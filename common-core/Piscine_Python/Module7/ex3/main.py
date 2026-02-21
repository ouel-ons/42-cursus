from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main() -> None:
    print("=== DataDeck Game Engine ===")
    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:", factory.get_supported_types())

    print("Simulating aggressive turn...")
    print("Hand:", [f"{c.name} ({c.cost})" for c in engine.hand])

    turn_result = engine.simulate_turn()
    print("Turn execution:")
    print("Strategy:", turn_result["strategy"])
    print("Actions:", turn_result["actions"])

    print("Game Report:")
    print(engine.get_engine_status())

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__": 
    main()
