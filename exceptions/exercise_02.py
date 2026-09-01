"""
Exercise 02: Specific exception
TODO: Implement parse_int(text).
      Return int(text). If that raises ValueError, return "Invalid number".
"""


def parse_int(text):
    # TODO: try int(text), except ValueError
    pass


def main() -> None:
    print(parse_int("42"))
    print(parse_int("invalid"))


if __name__ == "__main__":
    main()
