class Plant:
    """
    A class to represent a plant.
    """
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]

    for plant in plants:
        print(plant)
    print("")
    print(f"Total plants created: {len(plants)}")
