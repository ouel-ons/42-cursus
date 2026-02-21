from typing import Dict, List

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        health: int,
        mana_pool: int = 0,
    ) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(attack_power, int) or attack_power <= 0:
            raise ValueError("attack_power must be a positive integer.")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("health must be a positive integer.")
        if not isinstance(mana_pool, int) or mana_pool < 0:
            raise ValueError("mana_pool must be a non-negative integer.")

        self.attack_power: int = attack_power
        self.health: int = health
        self.mana_pool: int = mana_pool

    # ---- Card ----
    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite unit enters play with combat + magic abilities",
        }

    # ---- Combatable ----
    def attack(self, target) -> Dict:
        target_name = str(target) if target is not None else "Unknown"
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> Dict:
        if not isinstance(incoming_damage, int) or incoming_damage < 0:
            raise ValueError("incoming_damage must be a non-negative integer.")

        # Simple block rule (keep logic simple as required)
        blocked = min(3, incoming_damage)
        taken = incoming_damage - blocked
        self.health -= taken

        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> Dict:
        return {"attack": self.attack_power, "health": self.health}

    # ---- Magical ----
    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        if not isinstance(spell_name, str) or not spell_name:
            raise ValueError("spell_name must be a non-empty string.")
        if not isinstance(targets, list):
            raise ValueError("targets must be a list.")

        mana_used = min(4, self.mana_pool)  # keep consistent with subject example vibe
        self.mana_pool -= mana_used

        clean_targets: List[str] = [str(t) for t in targets if t is not None]

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": clean_targets,
            "mana_used": mana_used,
        }

    def channel_mana(self, amount: int) -> Dict:
        if not isinstance(amount, int) or amount < 0:
            raise ValueError("amount must be a non-negative integer.")
        self.mana_pool += amount
        return {"channeled": amount, "total_mana": self.mana_pool}

    def get_magic_stats(self) -> Dict:
        return {"mana_pool": self.mana_pool}
