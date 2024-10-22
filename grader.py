"""
Library providing functions to automatically grade student homeworks.
"""

import argparse
import doctest
import importlib
from os.path import abspath
from os.path import dirname
from os.path import join
from os.path import splitext
import subprocess
import sys
import unittest

HW_DIR = dirname(abspath(__file__))


def prepend_hw_path(filename, path=HW_DIR):
    """Prepend the homework's path in case the grader is called from outside."""
    return join(path, filename)

class TestCaseWithDoctests(unittest.TestCase):
    """Subclass this Test class if doctests should be checked."""
    def test_doctests(self):
        """Ensure doctests are present and pass."""
        module = importlib.import_module(splitext(self.target)[0])
        r = doctest.testmod(module)
        self.assertTrue(r.attempted, f'{self.target} does not have a doctest')
        self.assertFalse(r.failed, f'{self.target} contains failing doctests')


def grade_by_io(script, in_data, expected, points=1):
    """Grade a submitted example."""
    script = prepend_hw_path(script)
    process = subprocess.Popen(["python", script],
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    out, err = process.communicate(in_data.encode("utf-8"))
    actual = out.decode("utf-8")
    if expected.split() != actual.split():
        points = 0
    print(f'{points} points for {script}')
    if not points:
        if err:
            print("error:\n", err.decode('utf-8'))
        else:
            print("actual:\n", actual)
            print("expected:\n", expected)
    return points


def import_modules(host, modules):
    """
    Import modules to individual hw?_grader.

    Allows running the grader if not all modules are present. Otherwise,
    the interpreter would crash if any of the import files were missing.
    """
    for module in modules:
        module = splitext(module)[0]  # make sure to strip filename extensions
        try:
            setattr(host, module, importlib.import_module(module))
        except ModuleNotFoundError as e:
            print(e)
            print(f'{module} not found, 0 points', file=sys.stderr)


def calc_points(result, abort_on_error):
    """Return the number of points obtained by the given result"""
    total = result.testsRun
    successes = total - len(result.errors) - len(result.failures)
    points = successes / total * result.points
    if abort_on_error:
        if successes < total:
            sys.exit(1)
    print(points, "points for", result.target)
    return points


def grade(tests):
    parser = argparse.ArgumentParser()
    parser.add_argument('--module',
                    choices=sorted(test.target for test in tests),
                    help='select the module to test (default: all)')
    args = parser.parse_args()
    sys.argv = [sys.argv[0]]  # avoid problems in case a test uses argparse
    if args.module:  # only run selected test
        tests = (test for test in tests if test.target == args.module)

    total = 0.0
    for test in tests:
        modulename = splitext(test.target)[0]
        try:
            exec(f'import {modulename}')
        except ModuleNotFoundError:
            if args.module:  # abort on error if only one module is tested
                sys.exit(1)
            continue
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(test)
        runner = unittest.TextTestRunner()
        result = runner.run(suite)
        result.target = test.target
        result.points = test.points
        total += calc_points(result, args.module)

    print()
    print(total, "points in total")


def main():
    """Print error message telling students to call the individual graders instead."""
    print('library only for importing, call')
    print('python3 hw?_grader.py*')
    print('instead')


if __name__ == "__main__":
    sys.exit(main())
