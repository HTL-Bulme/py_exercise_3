import unittest

from . import FILENAME

import vrptw_reader


class TestPolarCoordinates(unittest.TestCase):
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

