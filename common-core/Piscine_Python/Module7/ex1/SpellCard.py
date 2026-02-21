from typing import Dict, List
from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(effect_type, str) or not effect_type:
            raise ValueError("effect_type must be a non-empty string.")
        self.effect_type: str = effect_type

    def play(self, game_state: Dict) -> Dict:
        effect_map = {
            "damage": f"Deal {self.cost} damage to target",
            "heal": f"Heal {self.cost} health to target",
            "buff": f"Buff target by +{self.cost}",
            "debuff": f"Debuff target by -{self.cost}",
        }
        effect_desc = effect_map.get(self.effect_type, "Unknown spell effect")

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect_desc,
        }

    def resolve_effect(self, targets: List[str]) -> Dict:
        if not isinstance(targets, list):
            raise ValueError("targets must be a list.")
        clean_targets: List[str] = []
        for t in targets:
            if isinstance(t, str) and t:
                clean_targets.append(t)

        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": clean_targets,
            "resolved": True,
        }
