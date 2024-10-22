#!/usr/bin/env python3

import io
import math
import sys
import unittest

import vrptw_reader
import vrp_solver

from grader import TestCaseWithDoctests

FILENAME = "R101.json"


class TestVRPTWReader(TestCaseWithDoctests):
    target = "vrptw_reader.py"
    points = 2

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


class TestDistanceMatrix(unittest.TestCase):
    target = "vrptw_reader.py"
    points = 1

    def setUp(self):
        self.problem = vrptw_reader.read_json(FILENAME)
        self.d = vrptw_reader.calc_distance_matrix([self.problem['depot']] +
                                                   self.problem['clients'])

    def test_docstring(self):
        self.assertTrue(len(vrptw_reader.calc_distance_matrix.__doc__) > 50)
        self.assertIn(">>>", vrptw_reader.calc_distance_matrix.__doc__)

    def test_distances(self):
        self.assertEqual(len(self.d), 26, 'distance matrix does not have 26 rows')
        self.assertEqual(len(self.d[0]), 26, 'distance matrix does not have 26 columns')
        self.assertAlmostEqual(self.d[0][5], math.hypot(20, 5))
        self.assertAlmostEqual(self.d[5][5], 0.0, 'distance of a point to itself must be 0.0')
        self.assertAlmostEqual(self.d[5][12], math.hypot(35, 5))

    def test_consecutive(self):
        flawed = [self.problem['depot']]
        flawed += self.problem['clients'][:10]
        flawed += self.problem['clients'][12:]
        self.assertRaises(AssertionError, vrptw_reader.calc_distance_matrix,
                          flawed)
        flawed = [self.problem['depot']] + self.problem['clients']
        flawed[13]['id'] = 100
        with self.assertRaises(AssertionError,
                               msg='only allow consecutive ids'):
            vrptw_reader.calc_distance_matrix(flawed)


class TestPolarCoordinates(unittest.TestCase):
    target = "vrptw_reader.py"
    points = 1

    def setUp(self):
        self.problem = vrptw_reader.read_json(FILENAME)
        self.p = vrptw_reader.calc_polar_coordinates(self.problem['depot'],
                                                   self.problem['clients'])
        self.p_o = vrptw_reader.order(self.p)

    def test_docstring(self):
        self.assertTrue(len(vrptw_reader.calc_polar_coordinates.__doc__) > 50)
        self.assertIn(">>>", vrptw_reader.calc_polar_coordinates.__doc__)
        self.assertTrue(len(vrptw_reader.order.__doc__) > 50)
        self.assertIn(">>>", vrptw_reader.order.__doc__)

    def test_polar_coordinates(self):
        self.assertEqual(len(self.p), 26, 'the list of polar coordinates does not have 26 entries')
        self.assertEqual(self.p[0].id, 0), 'the depot does not have the id equal to 0'
        self.assertEqual(self.p[0].polar_coordinate.r, 0), 'the depot does not have the polar coordinates(0, 0)'
        self.assertEqual(self.p[0].polar_coordinate.phi, 0), 'the depot does not have the polar coordinates(0, 0)'
        self.assertEqual(self.p[2].id, 2), 'the second vertex does not have the id equal to 2'
        self.assertEqual(self.p[2].polar_coordinate.r, 18.0), 'the node with the id 2 does not have the polar coordinates(18.0, 4.71238898038469)'
        self.assertAlmostEqual(self.p[2].polar_coordinate.phi, 4.71238898038469), 'the node with the id 2 does not have the polar coordinates(18.0, 4.71238898038469)'
        self.assertEqual(len(self.p_o), 26, 'the list of ordered polar coordinates does not have 26 entries')
        self.assertEqual(self.p_o[2].id, 24), 'the second vertex in the ordered list does not have the id equal to 24'


class TestVRPSolver(TestCaseWithDoctests):
    target = "vrp_solver.py"
    points = 5

    def setUp(self):
        self.problem = vrptw_reader.read_json(FILENAME)
        self.orig_problem = vrptw_reader.read_json(FILENAME)
        self.solution = vrp_solver.solve_vrp(self.problem)
        self.d = vrptw_reader.calc_distance_matrix([self.problem['depot']] +
                                                   self.problem['clients'])

    def test_original_problem(self):
        self.assertEqual(len(self.problem['clients']),
                         len(self.orig_problem['clients']),
                         'Solver must not modify the original problem.')

    def test_docstring(self):
        self.assertTrue(vrp_solver.solve_vrp.__doc__)
        self.assertTrue(len(vrp_solver.solve_vrp.__doc__) > 100)
        self.assertIn('>>>', vrp_solver.solve_vrp.__doc__,
                      'missing doctest in solve_vrp')
        self.assertTrue(vrp_solver.print_routes.__doc__)
        self.assertTrue(len(vrp_solver.print_routes.__doc__) > 50)
        self.assertIn(">>>", vrp_solver.print_routes.__doc__,
                      'missing doctest in print_routes')

    def test_module_docstring(self):
        self.assertTrue(vrp_solver.__doc__)
        self.assertTrue(len(vrp_solver.__doc__) > 20)

    def test_solve_vrp_return_type(self):
        self.assertIsInstance(self.solution, list)
        self.assertIsInstance(self.solution[0], list)
        self.assertIsInstance(self.solution[-1], list)

    def test_solve_vrp_solution_quality(self):
        self.assertEqual(len(self.problem['clients']),
                         len(self.orig_problem['clients']),
                         'Solver must not modify the original problem.')
        self.assertTrue(len(self.solution) < len(self.problem['clients']) / 2,
                        'Average route length too short.')

    def test_solve_vrp_solution_correctness(self):
        for route in self.solution:
            self.assertTrue(len(route) >= 3)
            self.assertEqual(route[0]['id'], 0, 'Each route must start w/ the depot.')
            self.assertEqual(route[-1]['id'], 0, 'Each route must end w/ the depot.')
        all_ids = list(range(1, 26))  # all clients must be served exactly once
        for route in self.solution:
            for client in route[1:-1]:
                self.assertIn(client['id'], all_ids,
                              "No client can be served more than once.")
                all_ids.remove(client['id'])
        self.assertListEqual(all_ids, [],
                             "Some clients are not serviced.")

    def test_solve_vrp_solution_feasibility(self):
        for route in self.solution:
            total_demand = 0
            distance = 0.0
            for client in route[1:-1]:
                total_demand += client['demand']
            self.assertTrue(total_demand <= self.problem['truck_capacity'],
                            'total demand of a route exceeds truck capacity')
            for prev_index, client in enumerate(route[1:]):
                prev_id = route[prev_index]['id']
                client_id = client['id']
                try:
                    distance += self.d[prev_id][client_id]
                except IndexError:
                    self.assertFalse('Solver must not modify the original '
                                     'problem.')
            self.assertTrue(distance <= self.problem['truck_range'],
                            'total distance of a route exceeds truck range')

    def test_print_routes(self):
        orig_stdout = sys.stdout
        sys.stdout = io.StringIO()
        vrp_solver.print_routes(self.solution)
        sys.stdout.seek(0)
        output = sys.stdout.read()
        sys.stdout = orig_stdout
        self.assertTrue(len(output) > 50, "Solutions need to be printed.")
        route_strings = output.split('\n')
        self.assertTrue(route_strings[0].strip() == ('[0, 12, 24, 3, 9, 1, 20, 0]'), 'The solution is not correct.')
        self.assertTrue(route_strings[1].strip() == ('[0, 10, 11, 19, 7, 18, 8, 17, 0]'), 'The solution is not correct.')
        self.assertTrue(route_strings[2].strip() == ('[0, 5, 6, 16, 14, 0]'), 'The solution is not correct.')
        self.assertTrue(route_strings[3].strip() == ('[0, 13, 15, 2, 22, 21, 0]'), 'The solution is not correct.')
        self.assertTrue(route_strings[4].strip() == ('[0, 23, 4, 25, 0]'), 'The solution is not correct.')


def grader(result):
    """Return the number of points obtained by the result"""
    total = result.testsRun
    successes = total - len(result.errors) - len(result.failures)
    points = successes / total * result.points
    print(points, "points for", result.target)
    return points


if __name__ == "__main__":
    tests = (TestVRPTWReader,
             TestDistanceMatrix,
             TestPolarCoordinates,
             TestVRPSolver)
    total = 0.0
    for test in tests:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(test)
        runner = unittest.TextTestRunner()
        result = runner.run(suite)
        result.target = test.target
        result.points = test.points
        total += grader(result)
    print()
    print(total, "points in total")
