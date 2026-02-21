from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("=== DataDeck Deck Builder ===")
    print("Building deck with different card types...")

    deck = Deck()
    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))
    deck.add_card(SpellCard("Lightning Bolt", 3, "Common", "damage"))
    deck.add_card(ArtifactCard("Mana Crystal", 2, "Rare", 3, "+1 mana per turn"))

    print("Deck stats:", deck.get_deck_stats())

    deck.shuffle()
    print("Drawing and playing cards:")

    while True:
        try:
            card = deck.draw_card()
        except IndexError:
            break

        print(f"Drew: {card.name} ({card.__class__.__name__.replace('Card', '')})")
        result = card.play({})
        print("Play result:", result)

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
