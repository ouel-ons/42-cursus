from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===")
    print("Testing Abstract Base Class Design:\n")

    fire_dragon = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=5
    )

    print("CreatureCard Info:")
    print(fire_dragon.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")
    playable = fire_dragon.is_playable(6)
    print("Playable:", playable)

    if playable:
        result = fire_dragon.play({})
        print("Play result:", result)

    print("\nFire Dragon attacks Goblin Warrior:")
    attack_result = fire_dragon.attack_target("Goblin Warrior")
    print("Attack result:", attack_result)

    print("\nTesting insufficient mana (3 available):")
    print("Playable:", fire_dragon.is_playable(3))

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
