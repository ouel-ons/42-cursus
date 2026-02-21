from typing import Dict
from ex0.Card import Card


class CreatureCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int
    ) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("Attack must be a positive integer.")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health must be a positive integer.")

        self.attack: int = attack
        self.health: int = health

    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target: str) -> Dict:
        if not isinstance(target, str) or not target:
            raise ValueError("Target must be a non-empty string.")

        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }

    def get_card_info(self) -> Dict:
        info = super().get_card_info()
        info.update({
            "attack": self.attack,
            "health": self.health
        })
        return info
