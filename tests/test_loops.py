from tests.load_exercise import load_exercise

exercise_01 = load_exercise("loops", "exercise_01")
exercise_02 = load_exercise("loops", "exercise_02")
exercise_03 = load_exercise("loops", "exercise_03")
exercise_04 = load_exercise("loops", "exercise_04")
exercise_05 = load_exercise("loops", "exercise_05")
exercise_06 = load_exercise("loops", "exercise_06")


def test_exercise_01_numbers_with_range():
    assert exercise_01.numbers_with_range() == [0, 1, 2, 3, 4]


def test_exercise_02_collect_items():
    items = ["apple", "banana", "cherry"]
    assert exercise_02.collect_items(items) == ["apple", "banana", "cherry"]
    assert exercise_02.collect_items([]) == []


def test_exercise_03_countdown():
    assert exercise_03.countdown() == [5, 4, 3, 2, 1, 0]


def test_exercise_04_collect_until_stop():
    assert exercise_04.collect_until_stop(["a", "b", "stop", "c"]) == ["a", "b"]
    assert exercise_04.collect_until_stop(["stop"]) == []
    assert exercise_04.collect_until_stop(["x", "y"]) == ["x", "y"]


def test_exercise_05_odd_numbers_up_to_9():
    assert exercise_05.odd_numbers_up_to_9() == [1, 3, 5, 7, 9]


def test_exercise_06_indexed_items():
    assert exercise_06.indexed_items(["a", "b", "c"]) == [(0, "a"), (1, "b"), (2, "c")]
    assert exercise_06.indexed_items([]) == []
