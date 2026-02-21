from typing import Dict, List

from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List) -> List:
        targets = [str(t) for t in available_targets]
        if "Enemy Player" in targets:
            targets.remove("Enemy Player")
            return ["Enemy Player"] + targets
        return targets

    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        playable = sorted(hand, key=lambda c: getattr(c, "cost", 999))

        cards_played: List[str] = []
        mana_used = 0
        damage_dealt = 0

        for card in playable[:2]:
            cards_played.append(getattr(card, "name", "Unknown"))
            mana_used += int(getattr(card, "cost", 0))
            if hasattr(card, "attack"):
                damage_dealt += int(getattr(card, "attack", 0))
            elif hasattr(card, "attack_power"):
                damage_dealt += int(getattr(card, "attack_power", 0))
            else:
                damage_dealt += int(getattr(card, "cost", 0))

        targets_attacked = ["Enemy Player"] if damage_dealt > 0 else []

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt,
        }
