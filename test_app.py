"""Unit tests for addition calculator and main script (PyJen017)."""

import subprocess
import sys
from calculator import add


def run_script(filename):
    return subprocess.run(
        [sys.executable, filename],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )


def test_add_positive_numbers():
    assert add(10, 20) == 30
    assert add(5, 7) == 12


def test_add_negative_numbers():
    assert add(-10, -5) == -15
    assert add(-10, 20) == 10


def test_add_zero():
    assert add(0, 0) == 0
    assert add(100, 0) == 100


def test_add_floating_point():
    assert round(add(1.5, 2.3), 1) == 3.8


def test_main_runs_and_prints_result():
    result = run_script("main.py")
    assert result.returncode == 0
    assert "PyJen017" in result.stdout
    assert "Result: 15 + 25 = 40" in result.stdout
