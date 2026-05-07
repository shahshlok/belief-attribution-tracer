import asyncio
import json

import pytest

import miscons
from pydantic_models import Evidence, LLMDetectionResponse, NotionalMisconception


class DummyLLMResponse(LLMDetectionResponse):
    @classmethod
    def single(cls, label: str) -> "DummyLLMResponse":
        evidence = Evidence(line_number=1, code_snippet="int x = 0;")
        misconception = NotionalMisconception(
            inferred_category_name=label,
            student_thought_process="The student believes variables update automatically.",
            conceptual_gap="They confuse assignment with ongoing linkage.",
            error_manifestation="wrong output",
            confidence=0.9,
            evidence=[evidence],
        )
        return cls(misconceptions=[misconception])


def _write_student(root, name="StudentA"):
    student_dir = root / "authentic_seeded" / "a3" / name
    student_dir.mkdir(parents=True)
    for question in ["Q1", "Q2", "Q3", "Q4"]:
        (student_dir / f"{question}.java").write_text("public class Test {}")
    return student_dir


def _write_questions(root):
    questions_dir = root / "data" / "a3"
    questions_dir.mkdir(parents=True)
    for question in ["q1", "q2", "q3", "q4"]:
        (questions_dir / f"{question}.md").write_text("Question text")
    return questions_dir


@pytest.fixture()
def isolated_a3(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(miscons, "CURRENT_ASSIGNMENT", "a3")
    _write_questions(tmp_path)
    return tmp_path


@pytest.mark.asyncio
async def test_process_student_question_uses_detection_helper(isolated_a3, monkeypatch):
    _write_student(isolated_a3)

    async def dummy_detect(model, problem_description, student_code, strategy, use_reasoning=False):
        suffix = "-R" if use_reasoning else ""
        return DummyLLMResponse.single(label=f"{model}{suffix}")

    monkeypatch.setattr(miscons, "detect_for_file", dummy_detect)

    result = await miscons.process_student_question(
        student_id="StudentA",
        question="Q1",
        strategy="taxonomy",
        semaphore=asyncio.Semaphore(10),
        include_reasoning=True,
    )

    assert result["status"] == "success"
    assert result["student"] == "StudentA"
    assert result["question"] == "Q1"
    assert len(result["models"]) == 6


def test_get_student_list_respects_submission_dir(isolated_a3):
    _write_student(isolated_a3, "StudentA")
    _write_student(isolated_a3, "StudentB")

    students = miscons.get_student_list()

    assert students == ["StudentA", "StudentB"]


@pytest.mark.asyncio
async def test_run_detection_writes_outputs(isolated_a3, monkeypatch):
    _write_student(isolated_a3)
    output_dir = isolated_a3 / "detections" / "a3_multi"

    async def dummy_detect(model, problem_description, student_code, strategy, use_reasoning=False):
        return DummyLLMResponse.single(label=model)

    monkeypatch.setattr(miscons, "detect_for_file", dummy_detect)

    stats = await miscons.run_detection(
        students=["StudentA"],
        strategy="taxonomy",
        output_dir=output_dir,
        include_reasoning=False,
    )

    assert stats["total_processed"] == 4
    assert stats["successful"] == 4

    strategy_dir = output_dir / "taxonomy"
    files = list(strategy_dir.glob("StudentA_Q*.json"))
    assert len(files) == 4

    stats_file = strategy_dir / "_stats.json"
    assert stats_file.exists()
    loaded_stats = json.loads(stats_file.read_text())
    assert loaded_stats["strategy"] == "taxonomy"
