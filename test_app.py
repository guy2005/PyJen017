"""Unit tests for addition calculator and main script (PyJen017)."""

import subprocess
import sys
import unittest
from calculator import add


class TestCalculatorApp(unittest.TestCase):
    """Test suite for add function and main script."""

    def test_add_positive_numbers(self):
        self.assertEqual(add(10, 20), 30)
        self.assertEqual(add(5, 7), 12)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-10, -5), -15)
        self.assertEqual(add(-10, 20), 10)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(100, 0), 100)

    def test_add_floating_point(self):
        self.assertEqual(round(add(1.5, 2.3), 1), 3.8)

    def test_main_execution(self):
        result = subprocess.run(
            [sys.executable, "main.py"],
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("PyJen017", result.stdout)
        self.assertIn("Result: 15 + 25 = 40", result.stdout)


if __name__ == "__main__":
    unittest.main()
