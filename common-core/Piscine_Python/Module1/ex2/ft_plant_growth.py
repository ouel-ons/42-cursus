class Plant:
    """
    A class to represent a plant that can grow and age.
    """
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm: int) -> None:
        """Increase the plant's height."""
        self.height += cm

    def age_plant(self, days: int) -> None:
        """Increase the plant's age."""
        self.age += days

    def get_info(self) -> str:
        """Return the current status of the plant."""
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    plant = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    print(plant.get_info())
    total_growth = 0
    for _ in range(6):
        plant.grow(1)
        plant.age_plant(1)
        total_growth += 1
    print("=== Day 7 ===")
    print(plant.get_info())
    print(f"Growth this week: +{total_growth}cm")
