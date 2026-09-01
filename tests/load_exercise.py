import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_exercise(package, exercise):
    path = ROOT / package / "{}.py".format(exercise)
    spec = importlib.util.spec_from_file_location(
        "{}.{}".format(package, exercise),
        path,
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
