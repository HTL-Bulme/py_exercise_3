import math
import unittest

from . import FILENAME

import vrptw_reader


class TestDistanceMatrix(unittest.TestCase):
    def setUp(self):
        self.problem = vrptw_reader.read_json(FILENAME)
        self.d = vrptw_reader.calc_distance_matrix([self.problem['depot']] +
                                                   self.problem['clients'])

    def test_docstring(self):
        self.assertTrue(len(vrptw_reader.calc_distance_matrix.__doc__) > 50)
        self.assertIn(">>>", vrptw_reader.calc_distance_matrix.__doc__)

    def test_distances(self):
        self.assertEqual(len(self.d), 26,
                         'distance matrix does not have 26 rows')
        self.assertEqual(len(self.d[0]), 26,
                         'distance matrix does not have 26 columns')
        self.assertAlmostEqual(self.d[0][5],
                               math.hypot(20, 5))
        self.assertAlmostEqual(self.d[5][5], 0.0,
                               'distance of a point to itself must be 0.0')
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
