import random
from typing import Dict, List, Optional

from ex0.Card import Card


class Deck:
    def __init__(self) -> None:
        self._cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("card must be an instance of Card.")
        self._cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        if not isinstance(card_name, str) or not card_name:
            raise ValueError("card_name must be a non-empty string.")

        for i, c in enumerate(self._cards):
            if c.name == card_name:
                del self._cards[i]
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def draw_card(self) -> Card:
        if not self._cards:
            raise IndexError("Cannot draw from an empty deck.")
        return self._cards.pop(0)

    def get_deck_stats(self) -> Dict:
        total = len(self._cards)
        if total == 0:
            return {"total_cards": 0, "creatures": 0, "spells": 0, "artifacts": 0, "avg_cost": 0.0}
        creatures = sum(1 for c in self._cards if c.__class__.__name__ == "CreatureCard")
        spells = sum(1 for c in self._cards if c.__class__.__name__ == "SpellCard")
        artifacts = sum(1 for c in self._cards if c.__class__.__name__ == "ArtifactCard")
        avg_cost = sum(c.cost for c in self._cards) / total

        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": float(avg_cost),
        }

    def peek(self) -> Optional[Card]:
        return self._cards[0] if self._cards else None
