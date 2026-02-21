import random
from typing import Dict, List

from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self._cards: Dict[str, TournamentCard] = {}
        self._matches_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        if not isinstance(card, TournamentCard):
            raise TypeError("card must be a TournamentCard.")
        if card.card_id in self._cards:
            raise ValueError("Card ID already registered.")
        self._cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        if card1_id not in self._cards or card2_id not in self._cards:
            raise ValueError("Both card IDs must be registered.")
        if card1_id == card2_id:
            raise ValueError("A card cannot play against itself.")

        c1 = self._cards[card1_id]
        c2 = self._cards[card2_id]

        if c1.attack_power > c2.attack_power:
            winner, loser = c1, c2
        elif c2.attack_power > c1.attack_power:
            winner, loser = c2, c1
        else:
            winner, loser = random.choice([(c1, c2), (c2, c1)])

        winner.update_wins(1)
        loser.update_losses(1)

        self._matches_played += 1

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating,
        }

    def get_leaderboard(self) -> List[Dict]:
        ranked = sorted(self._cards.values(), key=lambda c: c.rating, reverse=True)
        return [
            {"name": c.name, "id": c.card_id, "rating": c.rating, "wins": c.wins, "losses": c.losses}
            for c in ranked
        ]

    def generate_tournament_report(self) -> Dict:
        total = len(self._cards)
        avg = 0
        if total > 0:
            avg = sum(c.rating for c in self._cards.values()) / total

        return {
            "total_cards": total,
            "matches_played": self._matches_played,
            "avg_rating": int(avg) if total > 0 else 0,
            "platform_status": "active" if total > 0 else "empty",
        }
