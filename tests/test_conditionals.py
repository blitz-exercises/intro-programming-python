import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tests.load_exercise import load_exercise

exercise_01 = load_exercise("conditionals", "exercise_01")
exercise_02 = load_exercise("conditionals", "exercise_02")
exercise_03 = load_exercise("conditionals", "exercise_03")
exercise_04 = load_exercise("conditionals", "exercise_04")
exercise_05 = load_exercise("conditionals", "exercise_05")
exercise_06 = load_exercise("conditionals", "exercise_06")


def test_exercise_01_is_positive():
    assert exercise_01.is_positive(3) is True
    assert exercise_01.is_positive(0) is False
    assert exercise_01.is_positive(-1) is False


def test_exercise_02_even_or_odd():
    assert exercise_02.even_or_odd(4) == "even"
    assert exercise_02.even_or_odd(7) == "odd"
    assert exercise_02.even_or_odd(0) == "even"


def test_exercise_03_letter_grade():
    assert exercise_03.letter_grade(100) == "A"
    assert exercise_03.letter_grade(90) == "A"
    assert exercise_03.letter_grade(89) == "B"
    assert exercise_03.letter_grade(80) == "B"
    assert exercise_03.letter_grade(79) == "C"
    assert exercise_03.letter_grade(70) == "C"
    assert exercise_03.letter_grade(69) == "D"
    assert exercise_03.letter_grade(60) == "D"
    assert exercise_03.letter_grade(59) == "F"
    assert exercise_03.letter_grade(0) == "F"


def test_exercise_04_classify():
    assert exercise_04.classify(4) == "positive even"
    assert exercise_04.classify(3) == "positive odd"
    assert exercise_04.classify(0) == "not positive"
    assert exercise_04.classify(-2) == "not positive"


def test_exercise_05_yes_or_no():
    assert exercise_05.yes_or_no(True) == "yes"
    assert exercise_05.yes_or_no(False) == "no"


def test_exercise_06_matches():
    assert exercise_06.matches(1) is True
    assert exercise_06.matches(9) is True
    assert exercise_06.matches(100) is True
    assert exercise_06.matches(0) is False
    assert exercise_06.matches(10) is False
    assert exercise_06.matches(50) is False


if __name__ == "__main__":
    import pytest

    raise SystemExit(pytest.main([__file__, "-v"]))
