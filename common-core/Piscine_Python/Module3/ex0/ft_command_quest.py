"""Exercise 0 - Command Quest."""

import sys


def main() -> None:
    """Process command line arguments."""
    print("=== Command Quest ===")

    if len(sys.argv) == 1:
        print("No arguments provided!")

    print(f"Program name: {sys.argv[0]}")

    if len(sys.argv) > 1:
        print(f"Arguments received: {len(sys.argv) - 1}")
        i = 1
        while i < len(sys.argv):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1

    print(f"Total arguments: {len(sys.argv)}")
    print()


if __name__ == "__main__":
    main()
