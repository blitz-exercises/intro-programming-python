"""
Exercise 03: Multiple except
TODO: Implement convert_and_divide(left, right).
      Convert both arguments with int(), then divide left by right.
      On ValueError return "invalid".
      On ZeroDivisionError return "zero".
"""


def convert_and_divide(left, right):
    # TODO: handle ValueError and ZeroDivisionError separately
    pass


def main() -> None:
    print(convert_and_divide("10", "2"))
    print(convert_and_divide("10", "0"))
    print(convert_and_divide("x", "2"))


if __name__ == "__main__":
    main()
