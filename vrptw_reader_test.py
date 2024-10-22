import doctest
import unittest

from . import FILENAME

import vrptw_reader


class TestVRPTWReader(unittest.TestCase):
    def setUp(self):
        self.problem = vrptw_reader.read_json(FILENAME)

    def test_read_json_depot(self):
        self.assertIn("depot", self.problem.keys())
        self.assertEqual(self.problem["depot"]["est"], 0.0)
        self.assertEqual(self.problem["depot"]["lst"], 230.0)
        self.assertEqual(self.problem["depot"]["id"], 0)
        self.assertEqual(self.problem["depot"]["x"], 35.0)
        self.assertEqual(self.problem["depot"]["y"], 35.0)

    def test_read_json_truck_capacity(self):
        self.assertIn("truck_capacity", self.problem.keys())
        self.assertEqual(self.problem["truck_capacity"], 85.0)

    def test_read_json_truck_range(self):
        self.assertIn("truck_range", self.problem.keys())
        self.assertEqual(self.problem["truck_range"], 250.0)

    def test_read_json_clients(self):
        self.assertIn("clients", self.problem.keys())
        self.assertEqual(len(self.problem["clients"]), 25)
        for c in self.problem["clients"]:
            if not c["id"] == 17: continue
            self.assertEqual(c["est"], 157.0)
            self.assertEqual(c["lst"], 167.0)
            self.assertEqual(c["id"], 17)
            self.assertEqual(c["x"], 5.0)
            self.assertEqual(c["y"], 30.0)

    def test_docstring(self):
        self.assertTrue(vrptw_reader.read_json.__doc__,
                        'read_json does not have a docstring')
        self.assertTrue(len(vrptw_reader.read_json.__doc__) > 50,
                        'docstring of read_json is too short')
        self.assertIn('>>>', vrptw_reader.read_json.__doc__,
                      'missing doctests in read_json')

    def test_module_docstring(self):
        self.assertTrue(vrptw_reader.__doc__, "docstring is missing")
        self.assertTrue(len(vrptw_reader.__doc__) > 20, "docstring is too short")

    def test_doctests(self):
        """Ensure doctests are present and pass."""
        r = doctest.testmod(vrptw_reader)
        self.assertTrue(r.attempted,
                        f'vrptw_reader.py does not have a doctest')
        self.assertFalse(r.failed,
                         f'vrptw_reader.py contains failing doctests')
