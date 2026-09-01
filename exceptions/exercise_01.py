"""
Exercise 01: try-except basics
TODO: Implement safe_divide(a, b).
      Return a / b. If b is 0, catch ZeroDivisionError and return
      "Cannot divide by zero".
"""


def safe_divide(a, b):
    # TODO: try the division, except ZeroDivisionError
    pass


def main() -> None:
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))


if __name__ == "__main__":
    main()
