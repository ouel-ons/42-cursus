"""Exercise 1 - Score Cruncher."""

import sys


def main() -> None:
    """Analyze player scores."""
    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py "
            "<score1> <score2> ..."
        )
        return

    scores = []

    try:
        for arg in sys.argv[1:]:
            scores.append(int(arg))
    except Exception as err:
        print(f"Error: {err}")
        return

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")
    print()


if __name__ == "__main__":
    main()
