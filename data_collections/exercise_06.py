"""
Exercise 06: Collection methods
TODO: Implement three helpers:
      sorted_copy(values) — return a new list sorted with .sort() or sorted().
      mapping_keys(mapping) — return the dict keys as a list.
      with_added(values, extra) — return a set of values after adding extra.
"""


def sorted_copy(values):
    # TODO: return a sorted list
    pass


def mapping_keys(mapping):
    # TODO: return list(mapping.keys())
    pass


def with_added(values, extra):
    # TODO: make a set, add extra, return the set
    pass


def main() -> None:
    print(sorted_copy([3, 1, 2]))
    print(mapping_keys({"a": 1, "b": 2}))
    print(with_added({1, 2}, 3))


if __name__ == "__main__":
    main()
