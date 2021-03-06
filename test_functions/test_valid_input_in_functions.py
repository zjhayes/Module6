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

    def test_score_input_test_score_above_range(self):
        results = validate_input_in_functions.score_input("Zachary", 101, "Above")
        expected = "Above"
        self.assertTrue(results == expected)

    def test_test_score_non_numeric(self):
        results = validate_input_in_functions.score_input("Zachary", "invalid input", "Non-numeric")
        expected = "Non-numeric"
        self.assertTrue(results == expected)

    def test_score_input_invalid_message(self):
        results = validate_input_in_functions.score_input("Zachary", "invalid input", "Invalid message works")
        expected = "Invalid message works"
        self.assertTrue(results == expected)


if __name__ == '__main__':
    unittest.main()
