import json
import random


def get_random_value():
    """
    Returns a random integer between 1,000 and 9,999 (inclusive).
    """
    return random.randint(1_000, 9_999)


if __name__ == "__main__":
    """Provide range of values for further operations."""
    values = [get_random_value(), get_random_value()]
    payload = {
        "min": min(values),
        "max": max(values),
    }
    print(json.dumps(payload))
