from typing import Dict

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
        self,
        card_id: str,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        health: int,
        base_rating: int = 1200,
    ) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(card_id, str) or not card_id:
            raise ValueError("card_id must be a non-empty string.")
        if not isinstance(attack_power, int) or attack_power <= 0:
            raise ValueError("attack_power must be a positive integer.")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("health must be a positive integer.")
        if not isinstance(base_rating, int) or base_rating <= 0:
            raise ValueError("base_rating must be a positive integer.")

        self.card_id: str = card_id
        self.attack_power: int = attack_power
        self.health: int = health

        self.wins: int = 0
        self.losses: int = 0
        self.rating: int = base_rating

    # ---- Card ----
    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament card enters competitive play",
        }

    # ---- Combatable ----
    def attack(self, target) -> Dict:
        target_name = str(target) if target is not None else "Unknown"
        return {
            "attacker": self.card_id,
            "attacker_name": self.name,
            "target": target_name,
            "damage": self.attack_power,
        }

    def defend(self, incoming_damage: int) -> Dict:
        if not isinstance(incoming_damage, int) or incoming_damage < 0:
            raise ValueError("incoming_damage must be a non-negative integer.")
        self.health -= incoming_damage
        return {"defender": self.card_id, "health_left": self.health, "still_alive": self.health > 0}

    def get_combat_stats(self) -> Dict:
        return {"attack_power": self.attack_power, "health": self.health}

    # ---- Rankable ----
    def calculate_rating(self) -> int:
        self.rating = max(1, 1200 + (self.wins * 16) - (self.losses * 16))
        return self.rating

    def update_wins(self, wins: int) -> None:
        if not isinstance(wins, int) or wins < 0:
            raise ValueError("wins must be a non-negative integer.")
        self.wins += wins
        self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        if not isinstance(losses, int) or losses < 0:
            raise ValueError("losses must be a non-negative integer.")
        self.losses += losses
        self.calculate_rating()

    def get_rank_info(self) -> Dict:
        return {"rating": self.rating, "wins": self.wins, "losses": self.losses}

    # ---- Tournament helpers ----
    def get_tournament_stats(self) -> Dict:
        return {
            "id": self.card_id,
            "name": self.name,
            "record": f"{self.wins}-{self.losses}",
            "rating": self.rating,
            "combat": self.get_combat_stats(),
        }
