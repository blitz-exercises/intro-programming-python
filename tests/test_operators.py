from tests.load_exercise import load_exercise

exercise_01 = load_exercise("operators", "exercise_01")
exercise_02 = load_exercise("operators", "exercise_02")
exercise_03 = load_exercise("operators", "exercise_03")
exercise_04 = load_exercise("operators", "exercise_04")
exercise_05 = load_exercise("operators", "exercise_05")
exercise_06 = load_exercise("operators", "exercise_06")


def test_exercise_01_arithmetic():
    result = exercise_01.arithmetic(10, 3)
    assert result is not None, "arithmetic() is not implemented yet"
    plus, minus, times, divide, floor, remainder = result
    assert plus == 13
    assert minus == 7
    assert times == 30
    assert divide == 10 / 3
    assert floor == 3
    assert remainder == 1


def test_exercise_02_compare():
    assert exercise_02.compare(3, 5) == (True, False, False, True)
    assert exercise_02.compare(5, 3) == (False, True, False, True)
    assert exercise_02.compare(4, 4) == (False, False, True, False)


def test_exercise_03_logical():
    assert exercise_03.logical(True, True) == (True, True, False)
    assert exercise_03.logical(True, False) == (False, True, False)
    assert exercise_03.logical(False, True) == (False, True, True)
    assert exercise_03.logical(False, False) == (False, False, True)


def test_exercise_04_apply_assignments():
    assert exercise_04.apply_assignments(10) == [15, 12, 24]
    assert exercise_04.apply_assignments(0) == [5, 2, 4]


def test_exercise_05_check_membership():
    assert exercise_05.check_membership("a", "cat") == (True, False)
    assert exercise_05.check_membership(9, [1, 2, 3]) == (False, True)
    assert exercise_05.check_membership(2, [1, 2, 3]) == (True, False)


def test_exercise_06_precedence_demo():
    assert exercise_06.precedence_demo() == (14, 20)
