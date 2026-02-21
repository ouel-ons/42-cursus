import random
from typing import Dict

from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.Card import Card

from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self._creature_pool = [
            ("Fire Dragon", 5, "Legendary", 7, 5),
            ("Goblin Warrior", 2, "Common", 2, 2),
        ]
        self._spell_pool = [
            ("Lightning Bolt", 3, "Common", "damage"),
            ("Fireball", 4, "Rare", "damage"),
        ]
        self._artifact_pool = [
            ("Mana Ring", 2, "Rare", 3, "+1 mana per turn"),
            ("Crystal Staff", 4, "Epic", 2, "Spells cost -1 (simple)"),
        ]

    def get_supported_types(self) -> Dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball", "lightning"],
            "artifacts": ["mana_ring", "staff", "crystal"],
        }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str) and name_or_power:
            for n, cost, rar, atk, hp in self._creature_pool:
                if n.lower() == name_or_power.lower():
                    return CreatureCard(n, cost, rar, atk, hp)

        n, cost, rar, atk, hp = random.choice(self._creature_pool)
        if isinstance(name_or_power, int) and name_or_power > 0:
            atk = name_or_power
        return CreatureCard(n, cost, rar, atk, hp)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str) and name_or_power:
            for n, cost, rar, et in self._spell_pool:
                if n.lower() == name_or_power.lower():
                    return SpellCard(n, cost, rar, et)

        n, cost, rar, et = random.choice(self._spell_pool)
        if isinstance(name_or_power, int) and name_or_power > 0:
            cost = name_or_power
        return SpellCard(n, cost, rar, et)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str) and name_or_power:
            for n, cost, rar, dur, eff in self._artifact_pool:
                if n.lower() == name_or_power.lower():
                    return ArtifactCard(n, cost, rar, dur, eff)

        n, cost, rar, dur, eff = random.choice(self._artifact_pool)
        if isinstance(name_or_power, int) and name_or_power > 0:
            dur = name_or_power
        return ArtifactCard(n, cost, rar, dur, eff)

    def create_themed_deck(self, size: int) -> Dict:
        if not isinstance(size, int) or size <= 0:
            raise ValueError("size must be a positive integer.")

        cards = []
        for _ in range(size):
            kind = random.choice(["creature", "spell", "artifact"])
            if kind == "creature":
                cards.append(self.create_creature())
            elif kind == "spell":
                cards.append(self.create_spell())
            else:
                cards.append(self.create_artifact())

        return {"theme": "fantasy", "size": size, "cards": cards}
