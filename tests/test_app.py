import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from app import add


class TestApp(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(10, 20), 30)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_zero(self):
        self.assertEqual(add(5, 0), 5)


if __name__ == "__main__":
    unittest.main()
