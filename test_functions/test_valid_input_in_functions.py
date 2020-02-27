import unittest
from more_functions import validate_input_in_functions


class ValidateInputTest(unittest.TestCase):
    def test_score_input_test_name(self):
        results = validate_input_in_functions.score_input("Zachary", 100)
        expected = "Zachary: 100"
        self.assertTrue(results == expected)

    def test_score_input_test_score_valid(self):
        results = validate_input_in_functions.score_input("Zachary", 40)
        expected = "Zachary: 40"
        self.assertTrue(results == expected)

    def test_score_input_test_score_below_range(self):
        results = validate_input_in_functions.score_input("Zachary", -1, "Below")
        expected = "Below"
        self.assertTrue(results == expected)


if __name__ == '__main__':
    unittest.main()
