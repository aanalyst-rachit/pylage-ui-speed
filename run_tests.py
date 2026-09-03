import sys
import os
import re
import inspect
import importlib
import importlib.util
from pathlib import Path

# Minimal pytest mock
class _PytestMock:
    class raises:
        def __init__(self, expected_exc, match=None):
            self.expected_exc = expected_exc
            self.match = match
        def __enter__(self):
            return self
        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type is None:
                raise AssertionError(f"Expected {self.expected_exc} was not raised")
            if not issubclass(exc_type, self.expected_exc):
                return False
            if self.match and not re.search(self.match, str(exc_val)):
                raise AssertionError(f"Exception message '{exc_val}' did not match pattern '{self.match}'")
            return True

    class mark:
        @staticmethod
        def parametrize(argnames, argvalues):
            def decorator(func):
                func._pytest_parametrize = (argnames, argvalues)
                return func
            return decorator

    @staticmethod
    def importorskip(modname):
        try:
            return importlib.import_module(modname)
        except ImportError:
            class _Skip(Exception): pass
            raise _Skip(f"Skipping because {modname} not installed")

sys.modules["pytest"] = _PytestMock()

repo_root = Path(__file__).resolve().parent
test_dir = repo_root / "test"

sys.path.insert(0, str(repo_root))
sys.path.insert(0, str(test_dir))

def run_test_file(file_path):
    spec = importlib.util.spec_from_file_location(file_path.stem, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[file_path.stem] = module
    spec.loader.exec_module(module)

    test_funcs = [
        (name, func) for name, func in inspect.getmembers(module, inspect.isfunction)
        if name.startswith("test_")
    ]

    passed = 0
    failed = 0
    skipped = 0
    for name, func in test_funcs:
        try:
            if hasattr(func, "_pytest_parametrize"):
                argnames, argvalues = func._pytest_parametrize
                if isinstance(argnames, str):
                    argnames = [a.strip() for a in argnames.split(",")]
                for val in argvalues:
                    if len(argnames) == 1:
                        func(val)
                    else:
                        func(*val)
            else:
                func()
            passed += 1
        except Exception as e:
            if "Skipping because" in str(e):
                skipped += 1
            else:
                failed += 1
                print(f"  FAILED: {name} -> {e}")

    return passed, failed, skipped

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else None

    if target:
        target_path = Path(target)
        if not target_path.is_absolute():
            target_path = repo_root / target
        test_files = [target_path]
    else:
        test_files = sorted(test_dir.glob("test_ui_kit_*.py"))

    total_passed = 0
    total_failed = 0

    for tf in test_files:
        p, f, s = run_test_file(tf)
        total_passed += p
        total_failed += f
        status = "OK" if f == 0 else "FAIL"
        skip_msg = f" ({s} skipped)" if s > 0 else ""
        print(f"[{status}] {tf.name}: {p} passed, {f} failed{skip_msg}")

    print(f"\nSummary: {total_passed} passed, {total_failed} failed across {len(test_files)} files.")
    sys.exit(1 if total_failed > 0 else 0)

if __name__ == "__main__":
    main()
