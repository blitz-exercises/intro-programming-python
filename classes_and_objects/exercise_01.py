"""
Exercise 01: Simple class
TODO: Define Person with a name attribute set in __init__ (no arguments besides self).
      name must be a non-empty string.
"""


class Person:
    def __init__(self):
        # TODO: set self.name to a string
        pass


def main() -> None:
    person = Person()
    print(person.name)


if __name__ == "__main__":
    main()
