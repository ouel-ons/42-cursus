"""Exercise 1: Higher Realm."""

from __future__ import annotations
from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Return a function that calls both spells with the same arguments."""
    def combined(*args, **kwargs):
        return spell1(*args, **kwargs), spell2(*args, **kwargs)

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Return a function that multiplies the result of base_spell."""
    def amplified(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier

    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Return a function that only casts the spell if condition is true."""
    def caster(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"

    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    """Return a function that runs all spells in order."""
    def sequence(*args, **kwargs):
        return [spell(*args, **kwargs) for spell in spells]

    return sequence


if __name__ == "__main__":
    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    def base_damage(target: str) -> int:
        del target
        return 10

    def has_mana(target: str) -> bool:
        del target
        return True

    print("Testing spell combiner...")
    combined_spell = spell_combiner(fireball, heal)
    result = combined_spell("Dragon")
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("Testing power amplifier...")
    mega_spell = power_amplifier(base_damage, 3)
    print(f"Original: {base_damage('Dragon')}, Amplified: {mega_spell('Dragon')}")

    print("Testing conditional caster...")
    safe_fireball = conditional_caster(has_mana, fireball)
    print(safe_fireball("Goblin"))

    print("Testing spell sequence...")
    sequence = spell_sequence([fireball, heal])
    print(sequence("Knight"))