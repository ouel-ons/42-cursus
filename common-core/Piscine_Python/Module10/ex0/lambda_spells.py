"""Exercise 0: Lambda Sanctum."""

from __future__ import annotations


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort artifacts by power descending."""
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Filter mages by minimum power."""
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Transform spell names."""
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """Return mage statistics."""
    max_power = max(mages, key=lambda m: m["power"])["power"]
    min_power = min(mages, key=lambda m: m["power"])["power"]
    avg_power = round(sum(map(lambda m: m["power"], mages)) / len(mages), 2)

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power,
    }


if __name__ == "__main__":
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
        {"name": "Fire Staff", "power": 92, "type": "staff"},
        {"name": "Shadow Ring", "power": 77, "type": "ring"},
    ]

    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)

    first = sorted_artifacts[0]
    second = sorted_artifacts[1]

    print(
        f"{first['name']} ({first['power']} power) "
        f"comes before {second['name']} ({second['power']} power)"
    )

    print("Testing spell transformer...")
    print(" ".join(spell_transformer(spells)))
