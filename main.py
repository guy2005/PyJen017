"""Simple Python addition program for PyJen017."""

import sys
from calculator import add

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def main():
    print("=" * 45)
    print("   PyJen017: Simple Addition Program")
    print("   Student ID: 6752410017")
    print("   Version: 2.0 (CI/CD Auto-Build)")
    print("=" * 45)

    num1 = 15
    num2 = 25
    result = add(num1, num2)

    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print(f"Result: {num1} + {num2} = {result}")
    print("-" * 45)
    print("Program executed successfully!")
    print("=" * 45)


if __name__ == "__main__":
    main()
