"""Exercise 0 - Agricultural Data Validation Pipeline."""


def check_temperature(temp_str: str) -> int | None:
    """Validate temperature string and return int if valid."""
    try:
        temp: int = int(temp_str)

        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
            return None
        if temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
            return None

        print(f"Temperature {temp}°C is perfect for plants!")
        return temp

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None


def test_temperature_input() -> None:
    """Run temperature validation tests."""
    print("=== Garden Temperature Checker ===\n")

    tests: list[str] = ["25", "abc", "100", "-50"]

    for value in tests:
        print(f"Testing temperature: {value}")
        check_temperature(value)
        print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
