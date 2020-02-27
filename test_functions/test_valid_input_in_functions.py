import unittest
from more_functions import validate_input_in_functions


class ValidateInputTest(unittest.TestCase):
    def test_score_input_test_name(self):
        results = validate_input_in_functions.score_input("Zachary", 100)
        expected = "Zachary: 100"
        self.assertTrue(results == expected)


if __name__ == '__main__':
    unittest.main()
