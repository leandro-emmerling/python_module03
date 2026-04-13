#!/usr/bin/env python3


import random


PLAYERS: list[str] = [
    "Alice", "bob", "Charlie", "dylan", "Emma",
    "Gregory", "john", "kevin", "Liam"
    ]


def main() -> None:
    """Run the main Program."""
    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {PLAYERS}")
    capitalized: list[str] = [name.capitalize() for name in PLAYERS]
    print(f"New list with all names capitalized: {capitalized}")
    only_cap: list[str] = [
        name for name in PLAYERS if name == name.capitalize()
        ]
    print(f"New list of capitalized names only: {only_cap}\n")
    score_dict: dict[str, int] = {
        name: random.randint(0, 1000) for name in capitalized
        }
    print(f"Score dict: {score_dict}")
    avg: float = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"Score average is {avg}")
    high_scores: dict[str, int] = {
        name: score for name, score in score_dict.items() if score > avg
        }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
