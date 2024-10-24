import unittest

import business


class TestInterest(unittest.TestCase):
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
