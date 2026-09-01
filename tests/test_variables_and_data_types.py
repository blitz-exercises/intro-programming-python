import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tests.load_exercise import load_exercise

exercise_01 = load_exercise("variables_and_data_types", "exercise_01")
exercise_02 = load_exercise("variables_and_data_types", "exercise_02")
exercise_03 = load_exercise("variables_and_data_types", "exercise_03")
exercise_04 = load_exercise("variables_and_data_types", "exercise_04")
exercise_05 = load_exercise("variables_and_data_types", "exercise_05")
exercise_06 = load_exercise("variables_and_data_types", "exercise_06")


def test_exercise_01_age_and_height():
    result = exercise_01.get_age_and_height()
    assert result is not None, "get_age_and_height() is not implemented yet"
    age, height = result
    assert type(age) is int, "age must be an int"
    assert type(height) is float, "height must be a float"


def test_exercise_02_format_greeting():
    assert exercise_02.format_greeting("Ada") == "Hello, Ada!"
    assert exercise_02.format_greeting("Alan") == "Hello, Alan!"


def test_exercise_03_combine_flags():
    assert exercise_03.combine_flags(True, True) == (True, True, False)
    assert exercise_03.combine_flags(True, False) == (False, True, False)
    assert exercise_03.combine_flags(False, True) == (False, True, True)
    assert exercise_03.combine_flags(False, False) == (False, False, True)


def test_exercise_04_to_int():
    assert exercise_04.to_int("42") == 42
    assert exercise_04.to_int(3.14) == 3
    assert exercise_04.to_int("0") == 0


def test_exercise_05_maybe_value():
    assert exercise_05.maybe_value(True) is None
    assert exercise_05.maybe_value(False) is not None


def test_exercise_06_example_values():
    result = exercise_06.example_values()
    assert result is not None, "example_values() is not implemented yet"
    number, decimal, text, flag = result
    assert type(number) is int
    assert type(decimal) is float
    assert type(text) is str
    assert type(flag) is bool


if __name__ == "__main__":
    import pytest

    raise SystemExit(pytest.main([__file__, "-v"]))
