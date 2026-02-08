"""Exercise 1 - Different Types of Errors."""


def garden_operations() -> None:
    """Demonstrate different Python errors."""
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as err:
        print(f"Caught ValueError: {err}")

    print("\nTesting ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError as err:
        print(f"Caught ZeroDivisionError: {err}")

    print("\nTesting FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError as err:
        print(f"Caught FileNotFoundError: {err}")

    print("\nTesting KeyError...")
    try:
        plants: dict[str, int] = {"tomato": 5}
        print(plants["missing_plant"])
    except KeyError as err:
        print(f"Caught KeyError: {err}")

    print("\nTesting multiple errors together...")
    try:
        int("abc")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")


def test_error_types() -> None:
    """Run all error demonstrations."""
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
