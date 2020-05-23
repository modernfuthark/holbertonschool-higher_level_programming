#!/usr/bin/python3
""" 6-max_integer_test: Unittesting file for function max_integer """
import unittest
mi = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_basic(self):
        """ Tests a basic list of ints
            Checks if the function will return:
                - 5 at the end
                - 5 in the start
                - 4, with a negative
                - 4.5, a float value
                - 5, with a duped value
        """
        self.assertEqual(mi([1, 2, 3, 4, 5]), 5)
        self.assertEqual(mi([1, 5, 3, 4, 2]), 5)
        self.assertEqual(mi([-1, 0, 1, 2, 4]), 4)
        self.assertEqual(mi([1, 2, 3, 4, 4.5]), 4.5)
        self.assertEqual(mi([1, 2, 3, 4, 5, 5]), 5)

    def test_single(self):
        """ Tests using a list of only 1 int
            Checks for:
                - A lone positive, 5
                - A lone negative, -2
        """
        self.assertEqual(mi([5]), 5)
        self.assertEqual(mi([-2]), -2)

    def test_empty(self):
        """ Tests for None """
        self.assertIsNone(mi([]))

    def test_type(self):
        """ Tests for TypeErrors
            Checks for:
                - TypeError with a string as input
                - TypeError with an inline string
        """
        self.assertRaises(TypeError, mi, "String")
        self.assertRaises(TypeError, mi, [1, 2, "Three", 4])
