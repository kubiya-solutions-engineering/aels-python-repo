import random


def get_random_value():
    """
    Returns a random integer between 1,000 and 9,999 (inclusive).
    """
    return random.randint(1_000, 9_999)


if __name__ == '__main__':
    print(f"Generated random value: {get_random_value()}")
