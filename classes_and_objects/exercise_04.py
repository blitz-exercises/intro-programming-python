"""
Exercise 04: Multiple instances
TODO: Define Person with __init__(self, name) and greet(self) -> "Hello, {name}!".
      Implement create_two_people() so it returns two Person instances with
      different names.
"""


class Person:
    def __init__(self, name):
        # TODO: set self.name
        pass

    def greet(self):
        # TODO: return the greeting
        pass


def create_two_people():
    # TODO: return two Person instances with different names
    pass


def main() -> None:
    first, second = create_two_people()
    print(first.greet())
    print(second.greet())


if __name__ == "__main__":
    main()
