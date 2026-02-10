class Plant:
    """Base class for all plants."""
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def describe_base(self) -> str:
        """Return base plant info."""
        return f"{self.height}cm, {self.age} days"


class Flower(Plant):
    """Specialized Flower class."""
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def describe(self) -> None:
        print(f"{self.name} (Flower): {self.describe_base()}, "
              f"{self.color} color")
        self.bloom()


class Tree(Plant):
    """Specialized Tree class."""
    def __init__(self, name: str, height: int, age: int, diameter: int):
        super().__init__(name, height, age)
        self.diameter = diameter

    def produce_shade(self, area: int) -> None:
        print(f"{self.name} provides {area} square meters of shade")

    def describe(self) -> None:
        print(f"{self.name} (Tree): {self.describe_base()}, "
              f"{self.diameter}cm diameter")
        self.produce_shade(78)


class Vegetable(Plant):
    """Specialized Vegetable class."""
    def __init__(self, name: str, height: int, age: int, season: str,
                 nutritional_value: str):
        super().__init__(name, height, age)
        self.harvest_season = season
        self.nutritional_value = nutritional_value

    def describe(self) -> None:
        print(f"{self.name} (Vegetable): {self.describe_base()}, "
              f"{self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")


def main() -> None:
    """Instantiate and describe all plants."""
    print("=== Garden Plant Types ===\n")

    plants = [
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 20, 15, "yellow"),
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 600, 3000, 60),
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 40, 70, "spring", "vitamin A")
    ]

    for plant in plants:
        plant.describe()
        print("")


if __name__ == "__main__":
    main()
