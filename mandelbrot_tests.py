import unittest

from mandelbrot import parse_complex
from typing import List

class TestComplexParser(unittest.TestCase):
    
    def test_parse_string_list_to_complex_number(self):
        
        # Arrange

        complex_as_string_list: List[str]  = ["1", "2"]
        complex_number = complex(1, 2)

        # Act

        complex_parsed = parse_complex(complex_as_string_list)

        # Assert
        self.assertEqual(complex_number, complex_parsed)


if __name__ == "__main__":
    unittest.main()
