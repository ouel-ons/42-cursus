"""Exercise 0: Lambda Sanctum."""

from __future__ import annotations


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort artifacts by power descending."""
    return sorted(artifacts, key=lambda artifact: artifact["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Return mages with power greater than or equal to min_power."""
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Add a decorative prefix and suffix to each spell name."""
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """Return max, min, and average mage power."""
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

    max_power = max(mages, key=lambda mage: mage["power"])["power"]
    min_power = min(mages, key=lambda mage: mage["power"])["power"]
    avg_power = round(
        sum(map(lambda mage: mage["power"], mages)) / len(mages),
        2,
    )
    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power,
    }


if __name__ == "__main__":
    artifacts_data = [
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
        {"name": "Fire Staff", "power": 92, "type": "staff"},
        {"name": "Shadow Ring", "power": 77, "type": "ring"},
    ]
    mages_data = [
        {"name": "Aeris", "power": 95, "element": "air"},
        {"name": "Pyra", "power": 72, "element": "fire"},
        {"name": "Terra", "power": 88, "element": "earth"},
    ]
    spells_data = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts_data)
    print(
        f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power) "
        f"comes before {sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)"
    )

    print("Testing power filter...")
    print(power_filter(mages_data, 80))

    print("Testing spell transformer...")
    print(*spell_transformer(spells_data))

    print("Testing mage stats...")
    print(mage_stats(mages_data))