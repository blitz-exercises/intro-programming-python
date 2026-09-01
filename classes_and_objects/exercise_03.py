"""
Exercise 03: Methods
TODO: Define Person with __init__(self, name) and greet(self).
      greet() must return "Hello, {self.name}!".
"""


class Person:
    def __init__(self, name):
        # TODO: set self.name
        pass

    def greet(self):
        # TODO: return the greeting
        pass


def main() -> None:
    person = Person("Ada")
    print(person.greet())


if __name__ == "__main__":
    main()
