#!/usr/bin/env python3


import sys


def parse_arguments() -> list[int]:
    """Parse and validate command-line arguments as integers."""
    if len(sys.argv) < 2:
        return []
    scores: list[int] = []
    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    return scores


def handle_stats(scores: list[int]) -> None:
    """Calculate and display statistics for the given scores."""
    if not scores:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
        return
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


def main() -> None:
    """Run the main program."""
    print("=== Player Score Analytics ===")
    handle_stats(parse_arguments())


if __name__ == "__main__":
    main()
