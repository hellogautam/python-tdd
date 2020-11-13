"""
This file demonstrates common uses for the Python unittest module
https://docs.python.org/3/library/unittest.html
"""
import random
import unittest
from main import sum


class TestSequenceFunctions(unittest.TestCase):
    """ This is one of potentially many TestCases """

    def setUp(self):
        self.seq = list(range(10))

    def test_empty_string(self):
        self.assertEqual(0, sum(""))

    def test_single_string(self):
        self.assertEqual(1, sum("1"))

    def test_double_string(self):
        self.assertEqual(3, sum("1,2"))

    def test_unknown_string(self):
        self.assertEqual(17, sum("1,2,5,9"))

    def test_newline_string(self):
        self.assertEqual(15, sum("1\n2,5\n7"))

    def test_delimeter_string(self):
        self.assertEqual(6, sum("//###\n1###2###3"))
        self.assertEqual(6, sum("//,\n1,2,3"))

    def test_negative_string(self):
        self.assertEqual("negatives not allowed: -2", sum("//###\n1###-2###3"))
        self.assertEqual("negatives not allowed: -2 -5 ", sum("//###\n1###-2###3###-5"))


if __name__ == '__main__':
    unittest.main()
