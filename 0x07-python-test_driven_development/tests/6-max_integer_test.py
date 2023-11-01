#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Unittest class for max_integer """
    def test_normal(self):
        """ Unittest normal case """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_same(self):
        """ Unittest same case """
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_no_args(self):
        """ Unittest no args case """
        self.assertEqual(max_integer(), None)

    def test_empty(self):
        """ Unittest empty case """
        self.assertEqual(max_integer([]), None)

    def test_negative(self):
        """ Unittest negative case"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_string(self):
        """ Unittest string case"""
        with self.assertRaises(TypeError):
            max_integer([1, "string", 2])

    def test_not_list(self):
        """ Unittest not a list case """
        with self.assertRaises(TypeError):
            max_integer(1.5)
    
    def test_one(self):
        """ Unittest one elemnt case """
        self.assertEqual(max_integer([4]), 4)
    
    def test_middle(self):
        """ Unittest max in the middle case """
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)


if __name__ == "__main__":
    unittest.main()
