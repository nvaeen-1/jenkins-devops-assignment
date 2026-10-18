import sys
import unittest
from pathlib import Path

sys.path.insert(
    0, str(Path(__file__).resolve().parents[1] / "src")
)

from app import add


class TestAdditionalValues(unittest.TestCase):

    def test_negative_and_positive_numbers(self):
        self.assertEqual(add(-10, 5), -5)

    def test_two_negative_numbers(self):
        self.assertEqual(add(-5, -3), -8)

    def test_decimal_numbers(self):
        self.assertAlmostEqual(add(2.5, 4.5), 7.0)

    def test_zero_and_negative_number(self):
        self.assertEqual(add(0, -5), -5)


if __name__ == "__main__":
    unittest.main()
