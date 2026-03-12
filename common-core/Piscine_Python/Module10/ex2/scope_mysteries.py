"""Exercise 2: Memory Depths."""

from __future__ import annotations
from collections.abc import Callable


def mage_counter() -> Callable:
    """Return a closure that counts how many times it is called."""
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    """Return a closure that accumulates power over time."""
    total_power = initial_power

    def accumulator(amount: int):
        nonlocal total_power
        total_power += amount
        return total_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    """Return a function that applies the chosen enchantment."""
    def enchanter(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchanter


def memory_vault() -> dict[str, Callable]:
    """Return store and recall functions using private closure storage."""
    storage: dict[str, object] = {}

    def store(key: str, value: object) -> None:
        storage[key] = value

    def recall(key: str) -> object:
        return storage.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    print("Testing enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))
