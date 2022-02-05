import unittest

from mandelbrot import parse_complex, norm_square, pixel_to_point
from typing import List

class TestComplexParser(unittest.TestCase):
    
    def test_parse_string_list_to_complex_number(self):
        
        # Arrange

        complex_as_string_list: List[str]  = ["1", "2"]
        complex_number: complex = complex(1, 2)

        # Act

        complex_parsed = parse_complex(complex_as_string_list)

        # Assert
        self.assertEqual(complex_number, complex_parsed)

class TestComplexArithmetics(unittest.TestCase):

    def test_calculate_square(self):

        c: complex = complex(1, 2)
        expected_norm_square: float = 5.0

        calculated_norm_square: float = norm_square(c)

        self.assertEqual(expected_norm_square, calculated_norm_square)

class TestPixelToPoint(unittest.TestCase):

    def test_pixel_to_point(self):

        bounds = (100, 200)
        pixel = (25, 175)
        upper_left = complex(-1.0, 1.0)
        lower_right = complex(1.0, -1.0)
        expected = complex(-0.5, -0.75)
        
        actual = pixel_to_point(bounds, pixel, upper_left, lower_right)

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
