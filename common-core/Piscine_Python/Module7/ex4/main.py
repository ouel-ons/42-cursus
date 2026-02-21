from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===")

    platform = TournamentPlatform()

    print("Registering Tournament Cards...")

    dragon = TournamentCard(
        card_id="dragon_001",
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack_power=7,
        health=5,
        base_rating=1200,
    )
    wizard = TournamentCard(
        card_id="wizard_001",
        name="Ice Wizard",
        cost=4,
        rarity="Epic",
        attack_power=6,
        health=6,
        base_rating=1150,
    )

    platform.register_card(dragon)
    platform.register_card(wizard)

    print(f"{dragon.name} (ID: {dragon.card_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print("-", "Rating:", dragon.rating)
    print("-", "Record:", f"{dragon.wins}-{dragon.losses}")

    print(f"{wizard.name} (ID: {wizard.card_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print("-", "Rating:", wizard.rating)
    print("-", "Record:", f"{wizard.wins}-{wizard.losses}")

    print("Creating tournament match...")
    match = platform.create_match("dragon_001", "wizard_001")
    print("Match result:", match)

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, row in enumerate(leaderboard, start=1):
        print(f"{i}. {row['name']} - Rating: {row['rating']} ({row['wins']}-{row['losses']})")

    print("Platform Report:")
    print(platform.generate_tournament_report())

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
