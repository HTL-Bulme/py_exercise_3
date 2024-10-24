import unittest

import equations

class TestEquations(unittest.TestCase):
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

