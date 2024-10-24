#!/usr/bin/env python3

from math import hypot, pi
import unittest

import addition
import business
import conversion
import equations
import geometry
import main
import rot13
import vrptw_reader


class TestEquations(unittest.TestCase):
    target = "equations.py"

    def test_equation(self):
        x1, x2 = equations.quadratic(1, 1, -6)
        if x1 == -3:
            x1, x2 = x2, x1
        self.assertEqual(x1, 2)
        self.assertEqual(x2, -3)
        x1, x2 = equations.quadratic(2, 2, -7.5)
        if x1 == -2.5:
            x1, x2 = x2, x1
        self.assertEqual(x1, 1.5)
        self.assertEqual(x2, -2.5)

    def test_complex(self):
        x1, x2 = equations.quadratic(1, 0, 4)
        if x1 == 2j:
            x1, x2 = x2, x1
        self.assertEqual(x1, -2j)
        self.assertEqual(x2, 2j)
        if x1 == 2j:
            x1, x2 = x2, x1
        x1, x2 = equations.quadratic(2, 2, 1)
        if x1 == -0.5-0.5j:
            x1, x2 = x2, x1
        self.assertEqual(x1, -0.5+0.5j)


class TestAddition(unittest.TestCase):
    target = "addition.py"

    def test_simple(self):
        self.assertEqual(addition.sum_to(0), 0)
        self.assertEqual(addition.sum_to(1), 1)

    def test_regular(self):
        self.assertEqual(addition.sum_to(10), 55)
        self.assertEqual(addition.sum_to(25), 325)
        self.assertEqual(addition.sum_to(30), 129)

    def test_illegal(self):
        self.assertRaises(AssertionError, addition.sum_to, -1)
        self.assertRaises(AssertionError, addition.sum_to, -17)


class TestConversion(unittest.TestCase):
    target = "conversion.py"

    def test_celsius2fahrenheit(self):
        self.assertEqual(conversion.celsius2fahrenheit(0), 32)
        self.assertAlmostEqual(conversion.celsius2fahrenheit(31), 87.8)
        self.assertAlmostEqual(conversion.celsius2fahrenheit(-12), 10.4)

    def test_fahrenheit2celsius(self):
        self.assertEqual(conversion.fahrenheit2celsius(0), -32 / 1.8)
        self.assertEqual(conversion.fahrenheit2celsius(32), 0)
        self.assertEqual(conversion.fahrenheit2celsius(99.2), 67.2 / 1.8)


class TestGeometry(unittest.TestCase):
    target = "geometry.py"

    def test_perimeter_right_triangle(self):
        self.assertEqual(geometry.perimeter_right_triangle(0, 0), 0.0)
        self.assertEqual(geometry.perimeter_right_triangle(4, 3), 12.0)

    def test_area_right_triangle(self):
        self.assertEqual(geometry.area_right_triangle(0, 0), 0.0)
        self.assertEqual(geometry.area_right_triangle(4, 3), 6.0)

    def test_perimeter_circle(self):
        self.assertAlmostEqual(geometry.perimeter_circle(0), 0.0)
        self.assertAlmostEqual(geometry.perimeter_circle(1), 2 * pi)
        self.assertAlmostEqual(geometry.perimeter_circle(2.5), 2.5 * 2 * pi)

    def test_area_circle(self):
        self.assertAlmostEqual(geometry.area_circle(0), 0.0)
        self.assertAlmostEqual(geometry.area_circle(1), pi)
        self.assertAlmostEqual(geometry.area_circle(2.5), 2.5 * 2.5 * pi)

    def test_surface_sphere(self):
        self.assertAlmostEqual(geometry.surface_sphere(0), 0.0)
        self.assertAlmostEqual(geometry.surface_sphere(1), 4 * pi)
        self.assertAlmostEqual(geometry.surface_sphere(2.5), 4 * pi * 2.5 * 2.5)

    def test_volume_sphere(self):
        self.assertAlmostEqual(geometry.volume_sphere(0), 0.0)
        self.assertAlmostEqual(geometry.volume_sphere(1), 4 / 3 * pi)
        self.assertAlmostEqual(geometry.volume_sphere(2.5), 4 / 3 * pi * 2.5**3)

    def test_surface_cylinder(self):
        self.assertAlmostEqual(geometry.surface_cylinder(0, 0), 0.0)
        self.assertAlmostEqual(geometry.surface_cylinder(1, 0), 2 * pi)
        self.assertAlmostEqual(geometry.surface_cylinder(0, 1), 0.0)
        self.assertAlmostEqual(geometry.surface_cylinder(1, 1), 4 * pi)
        self.assertAlmostEqual(geometry.surface_cylinder(2.2, 3),
                               2 * 2.2 * 2.2 * pi + 2 * 2.2 * pi * 3)

    def test_volume_cylinder(self):
        self.assertAlmostEqual(geometry.volume_cylinder(0, 0), 0.0)
        self.assertAlmostEqual(geometry.volume_cylinder(1, 0), 0.0)
        self.assertAlmostEqual(geometry.volume_cylinder(0, 1), 0.0)
        self.assertAlmostEqual(geometry.volume_cylinder(1, 1), pi)
        self.assertAlmostEqual(geometry.volume_cylinder(2.2, 3.1),
                               2.2 * 2.2 * pi * 3.1)

    def test_surface_cone(self):
        self.assertAlmostEqual(geometry.surface_cone(0, 0), 0.0)
        self.assertAlmostEqual(geometry.surface_cone(0, 1), 0.0)
        self.assertAlmostEqual(geometry.surface_cone(1, 1),
                               pi + hypot(1, 1) * pi)
        self.assertAlmostEqual(geometry.surface_cone(2.2, 3.1),
                               2.2 * 2.2 * pi + 2.2 * pi * hypot(2.2, 3.1))

    def test_volume_cone(self):
        self.assertAlmostEqual(geometry.volume_cone(0, 0), 0.0)
        self.assertAlmostEqual(geometry.volume_cone(1, 0), 0.0)
        self.assertAlmostEqual(geometry.volume_cone(0, 1), 0.0)
        self.assertAlmostEqual(geometry.volume_cone(1, 1), pi / 3.0)
        self.assertAlmostEqual(geometry.volume_cone(2.2, 3.1),
                               2.2 * 2.2 * pi * 3.1 / 3.0)


class TestInterest(unittest.TestCase):
    target = "business.py"

    def test_interest(self):
        self.assertAlmostEqual(business.interest(100, 0.1), 10)
        self.assertAlmostEqual(business.interest(100, 0.1, tax=0.2), 8)
        self.assertAlmostEqual(business.interest(100, 0.1, 2), 21)
        self.assertAlmostEqual(business.interest(100, 0.1, 2, 0.2), 16.64)

    def test_terminal_value(self):
        self.assertAlmostEqual(business.terminal_value(100, 0.1), 110)
        self.assertAlmostEqual(business.terminal_value(100, 0.1, tax=0.2), 108)
        self.assertAlmostEqual(business.terminal_value(100, 0.1, 2), 121)
        self.assertAlmostEqual(business.terminal_value(100, 0.1, 2, 0.2),
                               116.64)


class TestRot13(unittest.TestCase):
    target = "rot13.py"

    def setUp(self):
        self.s = "Never trust a program you don't have sources for."
        self.s_enc = "Arire gehfg n cebtenz lbh qba'g unir fbheprf sbe."

    def test_encode(self):
        self.assertEqual(rot13.encode(''), '')
        self.assertEqual(rot13.encode(rot13.encode('test')), 'test')
        self.assertEqual(rot13.encode(self.s), self.s_enc)
        self.assertEqual(rot13.encode(self.s_enc), self.s)

    def test_decode(self):
        self.assertEqual(rot13.decode(''), '')
        self.assertEqual(rot13.decode(rot13.decode('test')), 'test')
        self.assertEqual(rot13.decode(self.s), self.s_enc)
        self.assertEqual(rot13.decode(self.s_enc), self.s)


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

    def test_read_string_list_count(self):
        """Test if the correct number of entries is read."""
        strings = vrptw_reader.read_string_list()
        self.assertEqual(len(strings), 101)

    def test_read_string_list(self):
        """Test if data is read correctly."""
        n1 = '    1      35.00      35.00       0.00       0.00     230.00       0.00\n'
        n7 = '    7      25.00      30.00       3.00      99.00     109.00      10.00\n'
        n101 = '  101      18.00      18.00      17.00     185.00     195.00      10.00\n'
        strings = vrptw_reader.read_string_list('r102')
        self.assertEqual(strings[0], n1)
        self.assertEqual(strings[6], n7)
        self.assertEqual(strings[100], n101)


class TestVRPTWReader2(unittest.TestCase):
    target = "vrptw_reader.py (part 2)"

    def setUp(self):
        self.strings = vrptw_reader.read_string_list('r101')

    def test_get_demand(self):
        self.assertEqual(vrptw_reader.get_demand(self.strings, 1), 0.0)
        self.assertEqual(vrptw_reader.get_demand(self.strings, 9), 9.0)
        self.assertEqual(vrptw_reader.get_demand(self.strings, 101), 17.0)

    def test_calc_distance(self):
        self.assertAlmostEqual(vrptw_reader.calc_distance(self.strings, 1, 3),
                               18.0)
        self.assertAlmostEqual(vrptw_reader.calc_distance(self.strings, 1, 17),
                               hypot(25, 15))


class TestMain(unittest.TestCase):
    target = "main.py"

    def test_main(self):
        self.assertEqual(main.main(), 0)


def grader(result):
    """Return the number of points obtained by the result"""
    if result.wasSuccessful():
        print("1   point for", result.target)
        return 1
    else:
        total = result.testsRun
        successes = total - len(result.errors) - len(result.failures)
        points = successes / total
        print(points, "points for", result.target)
        return points

if __name__ == "__main__":
    #TODO: move to examples section
    tests = (
             TestPolynomials,
             TestAddition,
             TestConversion,
             TestGeometry,
             TestInterest,
             TestRot13,
             TestVRPTWReader,
             TestVRPTWReader2,
             TestMain)
    total = 0.0
    for test in tests:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(test)
        runner = unittest.TextTestRunner()
        result = runner.run(suite)
        result.target = test.target
        total += grader(result)
    print()
    print(total, "points in total")
