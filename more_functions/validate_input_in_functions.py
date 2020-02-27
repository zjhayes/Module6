
def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    """I don't know what this does
        :param test_name, name of the person being tested.
        :param test_score, the score earned on test, default 0.
        :param invalid_message, message to warn of invalid input, default 'Invalid test score, try again!'.
        :returns the message multiplied as a string
        """
    try:
        if 0 <= test_score <= 100:
            return "%s: %d" % (test_name, test_score)
        else:
            raise TypeError()
    except TypeError as err:
        return invalid_message
