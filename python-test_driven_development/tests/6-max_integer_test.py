#!/usr/bin/python3
"""Unittests for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Suite of tests for max_integer function"""

    def test_ordered_list(self):
        """Test an ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list"""
        self.assertEqual(max_integer([3, 1, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test when max is at the beginning"""
        self.assertEqual(max_integer([10, 5, 3]), 10)

    def test_one_element(self):
        """Test a single-element list"""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test a list with all negative numbers"""
        self.assertEqual(max_integer([-3, -1, -7, -5]), -1)

    def test_mixed_numbers(self):
        """Test a list with negative and positive numbers"""
        self.assertEqual(max_integer([-10, -5, 0, 5, 3]), 5)

    def test_floats(self):
        """Test a list with floats"""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_strings(self):
        """Test a list of strings (max should be alphabetically last)"""
        self.assertEqual(max_integer(["apple", "banana", "pear"]), "pear")

    def test_empty_string(self):
        """Test an empty string input"""
        self.assertIsNone(max_integer([]))

if __name__ == '__main__':
    unittest.main()
