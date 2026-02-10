# ft_garden_analytics.py

class Plant:
    """Base class for all plants."""

    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def grow(self, amount: int = 1):
        """Increase plant height by specified amount."""
        self.height += amount


class FloweringPlant(Plant):
    """Plant with flowers that can bloom."""

    def __init__(self, name: str, height: int, flower_color: str):
        super().__init__(name, height)
        self.flower_color = flower_color
        self.is_blooming = True


class PrizeFlower(FloweringPlant):
    """Flower that has prize points."""

    def __init__(self, name: str, height: int, flower_color: str,
                 prize_points: int):
        super().__init__(name, height, flower_color)
        self.prize_points = prize_points


class GardenManager:
    """Manages multiple gardens and analytics."""

    total_gardens = 0

    def __init__(self, owner: str):
        self.owner = owner
        self.plants = []
        GardenManager.total_gardens += 1

    class GardenStats:
        """Nested helper for calculating garden statistics."""

        @staticmethod
        def total_growth(plants: list) -> int:
            return len(plants)  # 1cm per grow call

        @staticmethod
        def total_score(plants: list) -> int:
            score = sum([p.height for p in plants])
            score += sum([getattr(p, 'prize_points', 0) for p in plants])
            return score

    def add_plant(self, plant: Plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self):
        """Grow every plant by 1cm and report growth."""
        print(f"{self.owner} is helping all plants grow...")
        for p in self.plants:
            p.grow()
            print(f"{p.name} grew 1cm")

    @classmethod
    def create_garden_network(cls, owners: list) -> list:
        """Create multiple garden managers."""
        return [cls(owner) for owner in owners]

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0

    def display_report(self):
        """Print detailed report of this garden."""
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")

        reg, flow, prize = 0, 0, 0
        for p in self.plants:
            if isinstance(p, PrizeFlower):
                bloom_status = "blooming" if p.is_blooming else "not blooming"
                print(f"- {p.name}: {p.height}cm, {p.flower_color} "
                      f"flowers ({bloom_status}), "
                      f"Prize points: {p.prize_points}")
                prize += 1
            elif isinstance(p, FloweringPlant):
                bloom_status = "blooming" if p.is_blooming else "not blooming"
                print(f"- {p.name}: {p.height}cm, {p.flower_color} "
                      f"flowers ({bloom_status})")
                flow += 1
            else:
                print(f"- {p.name}: {p.height}cm")
                reg += 1

        print("")
        total_growth = self.GardenStats.total_growth(self.plants)
        print(f"Plants added: {len(self.plants)}, "
              f"Total growth: {total_growth}cm")
        print(f"Plant types: {reg} regular, {flow} flowering, "
              f"{prize} prize flowers\n")


def main():
    print("=== Garden Management System Demo ===\n")
    managers = GardenManager.create_garden_network(["Alice", "Bob"])
    alice = managers[0]
    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
    print("")
    bob = managers[1]
    bob.add_plant(Plant("Maple", 120))
    bob.add_plant(FloweringPlant("Tulip", 20, "pink"))
    bob.add_plant(PrizeFlower("Daisy", 30, "white", 5))
    print("")
    # Grow plants
    for manager in managers:
        manager.grow_all()
        print("")

    # Display reports
    for manager in managers:
        manager.display_report()

    # Height validation test
    print(f"Height validation test: {GardenManager.validate_height(10)}")

    # Display garden scores in required format
    scores = [
        f"{m.owner}: {m.GardenStats.total_score(m.plants)}"
        for m in managers
    ]
    print("Garden scores - " + ", ".join(scores))

    # Total gardens managed
    print(f"Total gardens managed: {GardenManager.total_gardens}")


if __name__ == "__main__":
    main()
