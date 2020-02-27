import unittest
from more_functions import string_functions


class StringFunctionTests(unittest.TestCase):
    def test_multiple_string(self):
        result = string_functions.multiply_strings("Aya", 4)
        self.assertEqual(result, "AyaAyaAyaAya")


if __name__ == '__main__':
    unittest.main()
