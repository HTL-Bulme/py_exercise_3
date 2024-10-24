from math import hypot
import unittest

from pytest import approx

import vrptw_reader


class TestVRPTWReader(unittest.TestCase):
    target = "vrptw_reader.py"

    def test_read_string_list_default(self):
        """Test default instance name."""
        strings = vrptw_reader.read_string_list()
        strings2 = vrptw_reader.read_string_list('r101')
        self.assertEqual(strings, strings2)

    def test_read_string_list_extension(self):
        """Test automatic addition of filename extension."""
        strings = vrptw_reader.read_string_list('r102')
        strings2 = vrptw_reader.read_string_list('r102.txt')
        self.assertEqual(strings, strings2)

    def test_read_string_list(self):
        """Test if the correct number of entries is read."""
        strings = vrptw_reader.read_string_list()
        self.assertEqual(len(strings), 101)

    def test_read_string_list_count(self):
        """Test if data is read correctly."""
        n1 = '    1      35.00      35.00       0.00       0.00     230.00       0.00\n'
        n7 = '    7      25.00      30.00       3.00      99.00     109.00      10.00\n'
        n101 = '  101      18.00      18.00      17.00     185.00     195.00      10.00\n'
        strings = vrptw_reader.read_string_list('r102')
        self.assertEqual(strings[0], n1)
        self.assertEqual(strings[6], n7)
        self.assertEqual(strings[100], n101)


def test_get_demand(self):
    strings = vrptw_reader.read_string_list('r101')
    assert vrptw_reader.get_demand(strings, 1) == 0.0
    assert vrptw_reader.get_demand(strings, 9) == 9.0
    assert vrptw_reader.get_demand(strings, 101) == 17.0

def test_calc_distance(self):
    assert vrptw_reader.calc_distance(self.strings, 1, 3) == approx(18.0)
    actual = vrptw_reader.calc_distance(self.strings, 1, 17)
    assert actual == approx(hypot(25, 15))
