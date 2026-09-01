"""
Exercise 06: Scope
TODO: Keep the global x as 10.
      Implement read_local_x() with a different local x and return that local value.
      Implement read_global_x() so it returns the global x.
"""

x = 10


def read_local_x():
    # TODO: create a local x (not 10) and return it
    pass


def read_global_x():
    # TODO: return the global x
    pass


def main() -> None:
    print(read_local_x())
    print(read_global_x())


if __name__ == "__main__":
    main()
