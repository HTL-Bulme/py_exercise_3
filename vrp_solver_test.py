import doctest
import io
import sys
import unittest

from . import FILENAME

import vrptw_reader
import vrp_solver


class TestVRPSolver(unittest.TestCase):
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

    def test_doctests(self):
        """Ensure doctests are present and pass."""
        r = doctest.testmod(vrp_solver)
        self.assertTrue(r.attempted, f'vrp_solver.py does not have a doctest')
        self.assertFalse(r.failed, f'vrp_solver.py contains failing doctests')
