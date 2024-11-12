# test_leading.py
import unittest
from leading import leading_substrings

class TestLeadingSubstrings(unittest.TestCase):
    
    def test_typical_case(self):
        """Test a regular string with multiple characters."""
        self.assertEqual(leading_substrings("bear"), ["b", "be", "bea", "bear"])

    def test_empty_string(self):
        """Test an empty string, should return an empty list."""
        self.assertEqual(leading_substrings(""), [])

    def test_single_character(self):
        """Test a single-character string."""
        self.assertEqual(leading_substrings("a"), ["a"])

    def test_repeated_characters(self):
        """Test a string with repeated characters."""
        self.assertEqual(leading_substrings("aaa"), ["a", "aa", "aaa"])

    def test_special_characters(self):
        """Test a string with special characters."""
        self.assertEqual(leading_substrings("a! "), ["a", "a!", "a! "])

if __name__ == "__main__":
    unittest.main()
