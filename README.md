# Intro Programming Python

A basic Python learning project covering core programming concepts through hands-on exercises.

## Prerequisites

- Python 3.8 or higher

```bash
pip install -r requirements.txt
```

## How to check your work

From the project root (`intro-programming-python/`):

```bash
pytest
```

Green means that exercise is correct. Red means it is not done yet, or the return value does not match the contract in the docstring.

Run one package or one test:

```bash
pytest tests/test_functions.py
pytest tests/test_functions.py::test_exercise_03_square
```

## How to Run Exercises

```bash
python -m variables_and_data_types.exercise_01
```

Or run a file directly:

```bash
python variables_and_data_types/exercise_01.py
```

## Package Summary

| Package | Topics |
|---------|--------|
| `variables_and_data_types` | int, float, str, bool, type(), type conversion, None |
| `functions` | def, parameters, return, default args, scope |
| `collections` | list, dict, tuple, set; indexing, slicing, methods |
| `operators` | arithmetic, comparison, logical, assignment, membership |
| `conditionals` | if/elif/else, nested conditions, ternary |
| `loops` | for, while, range(), break, continue, enumerate |
| `exceptions` | try/except, specific exceptions, raise, finally |
| `classes_and_objects` | class definition, __init__, self, methods, instances |
