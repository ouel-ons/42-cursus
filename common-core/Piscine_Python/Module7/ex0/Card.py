from abc import ABC, abstractmethod
from typing import Dict


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        if not isinstance(name, str) or not name:
            raise ValueError("Card name must be a non-empty string.")
        if not isinstance(cost, int) or cost < 0:
            raise ValueError("Card cost must be a non-negative integer.")
        if not isinstance(rarity, str) or not rarity:
            raise ValueError("Card rarity must be a non-empty string.")

        self.name: str = name
        self.cost: int = cost
        self.rarity: str = rarity

    @abstractmethod
    def play(self, game_state: Dict) -> Dict:
        """Play the card and modify the game state."""
        pass

    def get_card_info(self) -> Dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.__class__.__name__.replace("Card", "")
        }

    def is_playable(self, available_mana: int) -> bool:
        if not isinstance(available_mana, int) or available_mana < 0:
            raise ValueError("Available mana must be a non-negative integer.")
        return available_mana >= self.cost
