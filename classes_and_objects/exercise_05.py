"""
Exercise 05: Instance attributes
TODO: Define Person with __init__(self, name, age) and have_birthday(self).
      have_birthday() increases age by 1.
"""


class Person:
    def __init__(self, name, age):
        # TODO: set self.name and self.age
        pass

    def have_birthday(self):
        # TODO: increment self.age by 1
        pass


def main() -> None:
    person = Person("Ada", 36)
    person.have_birthday()
    print(person.name, person.age)


if __name__ == "__main__":
    main()
