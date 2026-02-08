"""Exercise 5 - Garden Management System."""


class GardenError(Exception):
    """Base garden error."""


class PlantError(GardenError):
    """Plant related error."""


class WaterError(GardenError):
    """Water related error."""


class GardenManager:
    """Simple garden management system."""

    def __init__(self) -> None:
        self.plants: list[str] = []

    def add_plant(self, plant_name: str) -> None:
        """Add plant to garden."""
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")

        self.plants.append(plant_name)
        print(f"Added {plant_name} successfully")

    def water_plants(self) -> None:
        """Water all plants with cleanup."""
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(
        self,
        plant: str,
        water_level: int,
        sun_hours: int
    ) -> None:
        """Check plant health."""
        if water_level > 10:
            raise WaterError(
                f"Water level {water_level} is too high (max 10)"
            )
        print(f"{plant}: healthy (water: {water_level}, sun: {sun_hours})")


def test_garden_management() -> None:
    """Run system tests."""
    print("=== Garden Management System ===\n")

    manager = GardenManager()

    try:
        manager.add_plant("tomato")
        manager.add_plant("lettuce")
        manager.add_plant("")
    except PlantError as err:
        print(f"Error adding plant: {err}")

    manager.water_plants()

    try:
        manager.check_plant_health("tomato", 5, 8)
        manager.check_plant_health("lettuce", 15, 8)
    except GardenError as err:
        print(f"Error checking plant: {err}")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
