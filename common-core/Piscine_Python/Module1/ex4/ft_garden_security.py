class SecurePlant:
    """
    A plant class with secure data access and validation.
    """
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self._height = height
        self._age = age
        print(f"Plant created: {self.name}")

    def get_height(self) -> int:
        """Safely return the height."""
        return self._height

    def set_height(self, height: int) -> None:
        """Set height with validation (must be non-negative)."""
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            print("")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm [OK]")

    def get_age(self) -> int:
        """Safely return the age."""
        return self._age

    def set_age(self, age: int) -> None:
        """Set age with validation (must be non-negative)."""
        if age < 0:
            print("Error: Age cannot be negative")
            print("")
        else:
            self._age = age
            print(f"Age updated: {self._age} days [OK]")
            print("")

    def __str__(self):
        return f"{self.name} ({self.get_height()}cm, {self.get_age()} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 0, 0)
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(30)
    print(f"Current plant: {plant}")

    p = SecurePlant("flower", 0, 0)
    p.set_height(20)
    p.set_age(89)
    p.set_height(30)
    print(f"Current plant: {p}")
