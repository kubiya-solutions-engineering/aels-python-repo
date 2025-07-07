import unittest
from source import get_random_value


class TestSource(unittest.TestCase):

    def test_value_in_range(self):
        """
        Tests if the generated value is within the expected range.
        This test should always pass.
        """
        for _ in range(3):
            with self.subTest():
                result = get_random_value()
                self.assertTrue(
                    1_000 <= result <= 9_999,
                    f"Value {result} out of range [1000, 9999]",
                )

    def test_failing_randomly(self):
        """
        This test is designed to fail approximately 50% of the time.
        It checks if the random number is even.
        """
        result = get_random_value()
        print(f"Testing if {result} is even for test_failing_randomly...")
        self.assertTrue(result % 2 == 0, f"Value {result} is not even, failing test.")

    def test_failing_always(self):
        """
        This test is designed to fail approximately 50% of the time.
        It checks if the random number is even.
        """
        for _ in range(3):
            with self.subTest():
                result = get_random_value()
                self.assertTrue(
                    (1_000 > result) or (result > 9_999),
                    f"Value {result} in range [1000, 9999]",
                )
