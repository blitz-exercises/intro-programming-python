import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tests.load_exercise import load_exercise

exercise_01 = load_exercise("exceptions", "exercise_01")
exercise_02 = load_exercise("exceptions", "exercise_02")
exercise_03 = load_exercise("exceptions", "exercise_03")
exercise_04 = load_exercise("exceptions", "exercise_04")
exercise_05 = load_exercise("exceptions", "exercise_05")
exercise_06 = load_exercise("exceptions", "exercise_06")


def test_exercise_01_safe_divide():
    assert exercise_01.safe_divide(10, 2) == 5
    assert exercise_01.safe_divide(10, 0) == "Cannot divide by zero"


def test_exercise_02_parse_int():
    assert exercise_02.parse_int("42") == 42
    assert exercise_02.parse_int("invalid") == "Invalid number"


def test_exercise_03_convert_and_divide():
    assert exercise_03.convert_and_divide("10", "2") == 5
    assert exercise_03.convert_and_divide("10", "0") == "zero"
    assert exercise_03.convert_and_divide("x", "2") == "invalid"
    assert exercise_03.convert_and_divide("10", "y") == "invalid"


def test_exercise_04_require_positive():
    assert exercise_04.require_positive(3) == 3
    assert exercise_04.require_positive(0) == 0
    with pytest.raises(ValueError, match="Number must be positive"):
        exercise_04.require_positive(-1)


def test_exercise_05_run_with_finally():
    assert exercise_05.run_with_finally(False) == ["try", "finally"]
    assert exercise_05.run_with_finally(True) == ["try", "except", "finally"]


def test_exercise_06_get_error_message():
    assert exercise_06.get_error_message("something went wrong") == "something went wrong"
    assert exercise_06.get_error_message("boom") == "boom"


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
