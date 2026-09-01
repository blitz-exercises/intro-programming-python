"""
Exercise 04: raise
TODO: Implement require_positive(n).
      If n is negative, raise ValueError with message "Number must be positive".
      Otherwise return n.
"""


def require_positive(n):
    # TODO: raise ValueError for negative n, else return n
    pass


def main() -> None:
    print(require_positive(3))
    try:
        require_positive(-1)
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
