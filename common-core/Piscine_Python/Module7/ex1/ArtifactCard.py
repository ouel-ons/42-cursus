from typing import Dict
from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(durability, int) or durability <= 0:
            raise ValueError("durability must be a positive integer.")
        if not isinstance(effect, str) or not effect:
            raise ValueError("effect must be a non-empty string.")
        self.durability: int = durability
        self.effect: str = effect

    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}",
        }

    def activate_ability(self) -> Dict:
        if self.durability <= 0:
            return {"artifact": self.name, "activated": False, "reason": "destroyed"}
        self.durability -= 1
        return {
            "artifact": self.name,
            "activated": True,
            "effect": self.effect,
            "durability_left": self.durability,
        }

    def get_card_info(self) -> Dict:
        info = super().get_card_info()
        info.update({"durability": self.durability, "effect": self.effect})
        return info
