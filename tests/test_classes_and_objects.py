import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tests.load_exercise import load_exercise

exercise_01 = load_exercise("classes_and_objects", "exercise_01")
exercise_02 = load_exercise("classes_and_objects", "exercise_02")
exercise_03 = load_exercise("classes_and_objects", "exercise_03")
exercise_04 = load_exercise("classes_and_objects", "exercise_04")
exercise_05 = load_exercise("classes_and_objects", "exercise_05")
exercise_06 = load_exercise("classes_and_objects", "exercise_06")


def test_exercise_01_person_has_name():
    person = exercise_01.Person()
    assert hasattr(person, "name"), "Person instance has no name attribute"
    assert type(person.name) is str
    assert person.name != ""


def test_exercise_02_person_init():
    person = exercise_02.Person("Ada")
    assert person.name == "Ada"
    assert exercise_02.Person("Alan").name == "Alan"


def test_exercise_03_person_greet():
    person = exercise_03.Person("Ada")
    assert person.greet() == "Hello, Ada!"
    assert exercise_03.Person("Alan").greet() == "Hello, Alan!"


def test_exercise_04_two_people():
    result = exercise_04.create_two_people()
    assert result is not None, "create_two_people() is not implemented yet"
    first, second = result
    assert isinstance(first, exercise_04.Person)
    assert isinstance(second, exercise_04.Person)
    assert first.name != second.name
    assert first.greet() == "Hello, {}!".format(first.name)
    assert second.greet() == "Hello, {}!".format(second.name)


def test_exercise_05_have_birthday():
    person = exercise_05.Person("Ada", 36)
    assert person.name == "Ada"
    assert person.age == 36
    person.have_birthday()
    assert person.age == 37
    person.have_birthday()
    assert person.age == 38


def test_exercise_06_rectangle_area():
    assert exercise_06.Rectangle(3, 4).area() == 12
    assert exercise_06.Rectangle(2, 5).area() == 10
    assert exercise_06.Rectangle(0, 9).area() == 0


if __name__ == "__main__":
    import pytest

    raise SystemExit(pytest.main([__file__, "-v"]))
