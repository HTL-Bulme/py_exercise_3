import unittest

import rot13


class TestRot13(unittest.TestCase):
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
