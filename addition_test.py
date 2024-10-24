import unittest

import addition


class TestAddition(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(addition.sum_to(0), 0)
        self.assertEqual(addition.sum_to(1), 1)
        self.assertEqual(addition.sum_to(2), 3)

    def test_regular(self):
        self.assertEqual(addition.sum_to(10), 55)
        self.assertEqual(addition.sum_to(25), 325)
        self.assertEqual(addition.sum_to(26), 351)

    def test_illegal(self):
        self.assertRaises(AssertionError, addition.sum_to, -1)
        self.assertRaises(AssertionError, addition.sum_to, -17)

def test_sum_to_slow():
    """Depending on your implementation, this test may take a while."""
    assert addition.sum_to(500000000) == 125000000250000000
