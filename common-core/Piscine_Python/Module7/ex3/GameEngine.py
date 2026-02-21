from typing import Dict, List, Optional

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from ex0.Card import Card


class GameEngine:
    def __init__(self) -> None:
        self._factory: Optional[CardFactory] = None
        self._strategy: Optional[GameStrategy] = None

        self._turns_simulated: int = 0
        self._total_damage: int = 0
        self._cards_created: int = 0

        self.hand: List[Card] = []
        self.battlefield: List[Card] = []

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        self._factory = factory
        self._strategy = strategy
        self.hand = [
            self._factory.create_creature("Fire Dragon"),
            self._factory.create_creature("Goblin Warrior"),
            self._factory.create_spell("Lightning Bolt"),
        ]
        self._cards_created = len(self.hand)

    def simulate_turn(self) -> Dict:
        if self._factory is None or self._strategy is None:
            raise RuntimeError("Engine must be configured with a factory and a strategy.")

        actions = self._strategy.execute_turn(self.hand, self.battlefield)
        self._turns_simulated += 1
        self._total_damage += int(actions.get("damage_dealt", 0))
        played_names = set(actions.get("cards_played", []))
        remaining_hand: List[Card] = []
        for c in self.hand:
            if c.name in played_names:
                self.battlefield.append(c)
            else:
                remaining_hand.append(c)
        self.hand = remaining_hand

        return {
            "strategy": self._strategy.get_strategy_name(),
            "actions": actions,
        }

    def get_engine_status(self) -> Dict:
        if self._factory is None or self._strategy is None:
            return {"configured": False, "turns_simulated": 0}

        return {
            "configured": True,
            "turns_simulated": self._turns_simulated,
            "strategy_used": self._strategy.get_strategy_name(),
            "total_damage": self._total_damage,
            "cards_created": self._cards_created,
            "hand_size": len(self.hand),
            "battlefield_size": len(self.battlefield),
        }
