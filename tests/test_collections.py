from tests.load_exercise import load_exercise

exercise_01 = load_exercise("collections", "exercise_01")
exercise_02 = load_exercise("collections", "exercise_02")
exercise_03 = load_exercise("collections", "exercise_03")
exercise_04 = load_exercise("collections", "exercise_04")
exercise_05 = load_exercise("collections", "exercise_05")
exercise_06 = load_exercise("collections", "exercise_06")


def test_exercise_01_add_item():
    assert exercise_01.add_item([1, 2, 3], 4) == [1, 2, 3, 4]
    assert exercise_01.add_item([], "a") == ["a"]


def test_exercise_02_first_last_slice():
    assert exercise_02.first_last_slice([10, 20, 30, 40]) == (10, 40, [20, 30])
    assert exercise_02.first_last_slice(["a", "b", "c", "d"]) == ("a", "d", ["b", "c"])


def test_exercise_03_get_age():
    ages = {"Ada": 36, "Alan": 41}
    assert exercise_03.get_age(ages, "Ada") == 36
    assert exercise_03.get_age(ages, "Alan") == 41


def test_exercise_04_unpack():
    assert exercise_04.unpack((1, 2, 3)) == (1, 2, 3)
    assert exercise_04.unpack(("a", "b", "c")) == ("a", "b", "c")


def test_exercise_05_unique():
    assert exercise_05.unique([1, 2, 2, 3, 3, 3]) == {1, 2, 3}
    assert exercise_05.unique(["a", "a", "b"]) == {"a", "b"}


def test_exercise_06_collection_methods():
    original = [3, 1, 2]
    assert exercise_06.sorted_copy(original) == [1, 2, 3]
    assert original == [3, 1, 2]

    keys = exercise_06.mapping_keys({"a": 1, "b": 2})
    assert set(keys) == {"a", "b"}
    assert len(keys) == 2

    assert exercise_06.with_added({1, 2}, 3) == {1, 2, 3}
    assert exercise_06.with_added(set(), "x") == {"x"}
