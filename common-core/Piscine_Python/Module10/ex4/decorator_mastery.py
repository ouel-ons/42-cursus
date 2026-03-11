"""Exercise 4: Master's Tower."""

from __future__ import annotations

import time
from functools import wraps


def spell_timer(func: callable) -> callable:
    """Decorator that measures execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> callable:
    """Decorator factory that validates power before casting."""
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get("power")

            if power is None:
                for value in reversed(args):
                    if isinstance(value, int):
                        power = value
                        break

            if power is None or power < min_power:
                return "Insufficient power for this spell"

            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> callable:
    """Retry a spell when it raises an exception."""
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 1
            while attempt <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == max_attempts:
                        return (
                            "Spell casting failed after "
                            f"{max_attempts} attempts"
                        )
                    print(
                        "Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
                    attempt += 1

        return wrapper

    return decorator


class MageGuild:
    """Simple class demonstrating staticmethod and decorators."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Return True when the name is at least 3 chars and valid."""
        cleaned = name.replace(" ", "")
        return len(name.strip()) >= 3 and cleaned.isalpha()

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell if enough power is provided."""
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    @retry_spell(3)
    def unstable_spell(counter: dict[str, int]) -> str:
        counter["tries"] += 1
        if counter["tries"] < 3:
            raise ValueError("Spell failed")
        return "Spell succeeded!"

    print("Testing spell timer...")
    print(f"Result: {fireball()}")

    print("Testing retry spell...")
    state = {"tries": 0}
    print(unstable_spell(state))

    print("Testing MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Ada"))
    print(MageGuild.validate_mage_name("A1"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))