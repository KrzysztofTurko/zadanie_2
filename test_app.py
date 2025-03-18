# test_app.py
import unittest
from app.py import is_valid_email, calculate_area, filter_even_numbers, convert_date_format, is_palindrome

class TestAppFunctions(unittest.TestCase):

    # Testy dla funkcji is_valid_email
    def test_is_valid_email(self):
        self.assertTrue(is_valid_email("test@example.com"))
        self.assertFalse(is_valid_email("invalid-email"))
        self.assertFalse(is_valid_email(""))

    # Testy dla funkcji calculate_area
    def test_calculate_area_rectangle(self):
        self.assertEqual(calculate_area('rectangle', 5, 10), 50)
        with self.assertRaises(ValueError):
            calculate_area('rectangle', 5)

    def test_calculate_area_circle(self):
        self.assertAlmostEqual(calculate_area('circle', 5), 78.5, places=1)
        with self.assertRaises(ValueError):
            calculate_area('circle', 5, 10)

    def test_calculate_area_triangle(self):
        self.assertEqual(calculate_area('triangle', 10, 5), 25)
        with self.assertRaises(ValueError):
            calculate_area('triangle', 10)

    # Testy dla funkcji filter_even_numbers
    def test_filter_even_numbers(self):
        self.assertEqual(filter_even_numbers([1, 2, 3, 4, 5]), [2, 4])
        self.assertEqual(filter_even_numbers([]), [])
        with self.assertRaises(TypeError):
            filter_even_numbers("not a list")

    # Testy dla funkcji convert_date_format
    def test_convert_date_format(self):
        self.assertEqual(convert_date_format("2023-10-05"), "05/10/2023")
        with self.assertRaises(ValueError):
            convert_date_format("2023/10/05")

    # Testy dla funkcji is_palindrome
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("kajak"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("not a palindrome"))
        with self.assertRaises(TypeError):
            is_palindrome(123)

if __name__ == '__main__':
    unittest.main()
