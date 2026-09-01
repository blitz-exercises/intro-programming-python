"""
Exercise 04: Default arguments
TODO: Implement greet(name, greeting="Hello") so it returns "{greeting}, {name}!".
      Examples: greet("Ada") -> "Hello, Ada!"
                greet("Ada", "Hi") -> "Hi, Ada!"
"""


def greet(name, greeting="Hello"):
    # TODO: return the greeting string
    pass


def main() -> None:
    print(greet("Ada"))
    print(greet("Ada", "Hi"))


if __name__ == "__main__":
    main()
