class Plant:
    """
    A class to represent a plant in the garden.
    """
    def __init__(self, name: str, height: int, age: int):
        """
        Initialize the plant with name, height, and age.
        """
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        """
        Return a string representation of the plant.
        """
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)

    print(plant1)
    print(plant2)
    print(plant3)
