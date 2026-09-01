from tests.load_exercise import load_exercise

exercise_01 = load_exercise("functions", "exercise_01")
exercise_02 = load_exercise("functions", "exercise_02")
exercise_03 = load_exercise("functions", "exercise_03")
exercise_04 = load_exercise("functions", "exercise_04")
exercise_05 = load_exercise("functions", "exercise_05")
exercise_06 = load_exercise("functions", "exercise_06")


def test_exercise_01_greet():
    assert exercise_01.greet("Ada") == "Hello, Ada!"
    assert exercise_01.greet("Alan") == "Hello, Alan!"


def test_exercise_02_add():
    assert exercise_02.add(2, 3) == 5
    assert exercise_02.add(-1, 1) == 0
    assert exercise_02.add(0, 0) == 0


def test_exercise_03_square():
    assert exercise_03.square(4) == 16
    assert exercise_03.square(0) == 0
    assert exercise_03.square(-3) == 9


def test_exercise_04_greet_default_argument():
    assert exercise_04.greet("Ada") == "Hello, Ada!"
    assert exercise_04.greet("Ada", "Hi") == "Hi, Ada!"


def test_exercise_05_min_max():
    assert exercise_05.min_max(3, 8) == (3, 8)
    assert exercise_05.min_max(9, 1) == (1, 9)
    assert exercise_05.min_max(4, 4) == (4, 4)


def test_exercise_06_scope():
    assert exercise_06.x == 10
    assert exercise_06.read_global_x() == 10
    local_value = exercise_06.read_local_x()
    assert local_value is not None, "read_local_x() is not implemented yet"
    assert local_value != 10, "local x should be different from the global x"
