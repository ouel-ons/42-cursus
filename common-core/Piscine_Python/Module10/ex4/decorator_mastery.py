"""Exercise 4: Master's Tower."""

from __future__ import annotations

import time
from functools import wraps


def spell_timer(func: callable) -> callable:
    """Decorator that measures function execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> callable:
    """Decorator factory that validates power before casting."""
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get("power")

            if power is None and len(args) >= 2:
                power = args[-1]

            if not isinstance(power, int) or power < min_power:
                return "Insufficient power for this spell"

            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> callable:
    """Decorator that retries a function if it raises an exception."""
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
    """Simple class demonstrating staticmethod usage."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Return True if name is valid."""
        cleaned_name = name.replace(" ", "")
        return len(name.strip()) >= 3 and cleaned_name.isalpha()

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell if the mage has enough power."""
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    @spell_timer
    def fireball() -> str:
        """Simple test spell."""
        time.sleep(0.101)
        return "Fireball cast!"

    print("Testing spell timer...")
    print(f"Result: {fireball()}")

    print("Testing MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Ada"))
    print(MageGuild.validate_mage_name("A1"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))
