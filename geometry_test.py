from math import hypot, pi
import unittest

import geometry


class TestGeometry(unittest.TestCase):
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
