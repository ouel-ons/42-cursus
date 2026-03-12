"""Exercise 3: Ancient Library."""

from __future__ import annotations

import functools
import operator
from collections.abc import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce spell powers using the requested operation."""
    if not spells:
        return 0

    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }

    if operation not in operations:
        raise ValueError("Unsupported operation")

    return functools.reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """Create specialized partial enchantment functions."""
    return {
        "fire_enchant": functools.partial(base_enchantment, 50, "fire"),
        "ice_enchant": functools.partial(base_enchantment, 50, "ice"),
        "lightning_enchant": functools.partial(
            base_enchantment,
            50,
            "lightning",
        ),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number using caching."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    """Create a singledispatch spell system."""
    @functools.singledispatch
    def dispatch(value):
        return "Unknown spell type"

    @dispatch.register
    def _(value: int):
        return f"Damage spell deals {value} damage"

    @dispatch.register
    def _(value: str):
        return f"Enchantment spell casts {value}"

    @dispatch.register
    def _(value: list):
        return [dispatch(item) for item in value]

    return dispatch


if __name__ == "__main__":
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("Testing memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
