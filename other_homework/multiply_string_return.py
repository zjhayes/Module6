# Zachary Hayes


def multiply_string(message, n):
    """Takes a message and echoes it back a given number of times."""
    return message * n


if __name__ == '__main__':
    try:  # check for ValueError
        print(multiply_string("Python!", 7))
    except ValueError as err:
        print("ValueError encountered!")
