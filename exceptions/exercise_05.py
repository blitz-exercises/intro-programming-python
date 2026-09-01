"""
Exercise 05: finally
TODO: Implement run_with_finally(should_fail).
      Append "try" first. If should_fail is True, raise ValueError and append
      "except" in the except block. Always append "finally" in the finally block.
      Return the list of events.
      Examples: run_with_finally(False) -> ["try", "finally"]
                run_with_finally(True)  -> ["try", "except", "finally"]
"""


def run_with_finally(should_fail):
    # TODO: use try/except/finally and return the event list
    pass


def main() -> None:
    print(run_with_finally(False))
    print(run_with_finally(True))


if __name__ == "__main__":
    main()
