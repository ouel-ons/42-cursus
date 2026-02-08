# ft_analytics_dashboard.py

from typing import TypedDict


class Player(TypedDict):
    name: str
    score: int
    active: bool
    region: str
    achievements: list[str]


def sample_players() -> list[Player]:
    """Return hardcoded sample player data."""
    return [
        {
            "name": "alice",
            "score": 2300,
            "active": True,
            "region": "north",
            "achievements": [
                "first_kill",
                "level_10",
                "boss_slayer",
                "collector",
                "speed_runner",
            ],
        },
        {
            "name": "bob",
            "score": 1800,
            "active": True,
            "region": "east",
            "achievements": ["first_kill", "collector", "explorer"],
        },
        {
            "name": "charlie",
            "score": 2150,
            "active": True,
            "region": "central",
            "achievements": [
                "first_kill",
                "level_10",
                "boss_slayer",
                "strategist",
                "survivor",
                "collector",
                "explorer",
            ],
        },
        {
            "name": "diana",
            "score": 2050,
            "active": False,
            "region": "north",
            "achievements": [
                "first_kill",
                "builder",
                "architect",
                "healer",
                "trader",
            ],
        },
    ]


def score_category(score: int) -> str:
    if score > 2000:
        return "high"
    if score >= 1500:
        return "medium"
    return "low"


def main() -> None:
    players = sample_players()

    print("=== Game Analytics Dashboard ===")
    print()
    # ----------------------------
    # List Comprehension Examples
    # ----------------------------
    print("=== List Comprehension Examples ===")
    high_scorers = [p["name"] for p in players if p["score"] > 2000]
    scores_doubled = [p["score"] * 2 for p in players]
    active_players = [p["name"] for p in players if p["active"]]

    print("High scorers (>2000): " + str(high_scorers))
    print("Scores doubled: " + str(scores_doubled))
    print("Active players: " + str(active_players))

    # ----------------------------
    # Dict Comprehension Examples
    # ----------------------------
    print()
    print("=== Dict Comprehension Examples ===")
    player_scores = {p["name"]: p["score"] for p in players if p["active"]}

    # Add two example boundary scores to match the exercise example breakdown.
    sample_scores = [p["score"] for p in players] + [1500, 1499]
    categories = [score_category(s) for s in sample_scores]
    score_categories = {
        c: len([x for x in categories if x == c])
        for c in {"high", "medium", "low"}
    }

    achievement_counts = {
        p["name"]: len(p["achievements"])
        for p in players
        if p["active"]
    }

    print("Player scores: " + str(player_scores))
    print("Score categories: " + str(score_categories))
    print("Achievement counts: " + str(achievement_counts))

    # ----------------------------
    # Set Comprehension Examples
    # ----------------------------
    print()
    print("=== Set Comprehension Examples ===")
    unique_players = {p["name"] for p in players}
    core_achievements = {"first_kill", "level_10", "boss_slayer"}
    unique_achievements = {
        a:  # type: ignore[misc]
        a
        for p in players
        for a in p["achievements"]
        if a in core_achievements
    }
    active_regions = {p["region"] for p in players if p["active"]}

    print("Unique players: " + str(unique_players))
    print("Unique achievements: " + str(unique_achievements))
    print("Active regions: " + str(active_regions))

    # ----------------------------
    # Combined Analysis
    # ----------------------------
    print()
    print("=== Combined Analysis ===")
    scores = [p["score"] for p in players]
    avg_score = sum(scores) / len(scores)

    all_achievements = {a for p in players for a in p["achievements"]}

    top = players[0]
    for p in players:
        if p["score"] > top["score"]:
            top = p

    print("Total players: " + str(len(players)))
    print("Total unique achievements: " + str(len(all_achievements)))
    print("Average score: " + str(avg_score))
    print(
        "Top performer: "
        + top["name"]
        + " ("
        + str(top["score"])
        + " points, "
        + str(len(top["achievements"]))
        + " achievements)"
    )


if __name__ == "__main__":
    main()
