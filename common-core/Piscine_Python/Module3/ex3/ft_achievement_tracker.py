"""Exercise 3 - Achievement Hunter."""


def main() -> None:
    print("=== Achievement Tracker System ===")
    print()
    alice: set[str] = set(
        [
            "first_kill",
            "level_10",
            "treasure_hunter",
            "speed_demon",
        ]
    )
    bob: set[str] = set(
        [
            "first_kill",
            "level_10",
            "boss_slayer",
            "collector",
        ]
    )
    charlie: set[str] = set(
        [
            "level_10",
            "treasure_hunter",
            "boss_slayer",
            "speed_demon",
            "perfectionist",
        ]
    )

    print("Player alice achievements:", alice)
    print("Player bob achievements:", bob)
    print("Player charlie achievements:", charlie)
    print()
    print("=== Achievement Analytics ===")

    all_ach: set[str] = alice.union(bob).union(charlie)
    print("All unique achievements:", all_ach)
    print("Total unique achievements:", len(all_ach))
    print()
    common_all: set[str] = alice.intersection(bob).intersection(charlie)
    print("Common to all players:", common_all)

    rare: set[str] = (
        alice.difference(bob.union(charlie))
        .union(bob.difference(alice.union(charlie)))
        .union(charlie.difference(alice.union(bob)))
    )
    print("Rare achievements (1 player):", rare)
    print()
    print("Alice vs Bob common:", alice.intersection(bob))
    print("Alice unique:", alice.difference(bob))
    print("Bob unique:", bob.difference(alice))


if __name__ == "__main__":
    main()
