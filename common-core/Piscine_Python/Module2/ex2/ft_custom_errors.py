"""Exercise 2 - Custom Garden Errors."""


class GardenError(Exception):
    """Base exception for garden problems."""


class PlantError(GardenError):
    """Exception for plant-related problems."""


class WaterError(GardenError):
    """Exception for watering-related problems."""


def check_plant() -> None:
    """Raise PlantError example."""
    raise PlantError("The tomato plant is wilting!")


def check_water() -> None:
    """Raise WaterError example."""
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    """Demonstrate custom exception handling."""
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        check_plant()
    except PlantError as err:
        print(f"Caught PlantError: {err}")

    print("\nTesting WaterError...")
    try:
        check_water()
    except WaterError as err:
        print(f"Caught WaterError: {err}")

    print("\nTesting catching all garden errors...")
    try:
        check_plant()
    except GardenError as err:
        print(f"Caught a garden error: {err}")

    try:
        check_water()
    except GardenError as err:
        print(f"Caught a garden error: {err}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
