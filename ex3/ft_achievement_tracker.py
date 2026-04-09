#!/usr/bin/env python3


import random


ACHIEVEMENTS: list[str] = [
    "First Steps", "Boss Slayer", "Speed Runner",
    "Survivor", "Master Explorer", "Treasure Hunter",
    "Untouchable", "Sharp Mind", "Strategist",
    "Collector Supreme", "World Savior", "Crafting Genius",
    "Unstoppable", "Hidden Path Finder", "Master Crafter"
]


def gen_player_achievements() -> set[str]:
    """Generate a random set of achievements"""
    num: int = random.randint(1, len(ACHIEVEMENTS))
    return set(random.sample(ACHIEVEMENTS, k=num))


def main() -> None:
    """Run the main program"""
    print("=== Achievement Tracker System ===\n")
    p1: set[str] = gen_player_achievements()
    p2: set[str] = gen_player_achievements()
    p3: set[str] = gen_player_achievements()
    p4: set[str] = gen_player_achievements()
    print(f"Player Alice: {p1}")
    print(f"Player Bob: {p2}")
    print(f"Player Charlie: {p3}")
    print(f"Player Dylan: {p4}")
    print(f"All distinct achievements: {set.union(p1, p2, p3, p4)}\n")
    print(f"Common achievements: {set.intersection(p1, p2, p3, p4)}\n")
    print(f"Only Alice has: {set.difference(p1, set.union(p2, p3, p4))}")
    print(f"Only Bob has: {set.difference(p2, set.union(p1, p3, p4))}")
    print(f"Only Charlie has: {set.difference(p3, set.union(p1, p2, p4))}")
    print(f"Only Dylan has: {set.difference(p4, set.union(p1, p2, p3))}\n")
    print(f"Alice is missing: {set.difference(set(ACHIEVEMENTS), p1)}")
    print(f"Bob is missing: {set.difference(set(ACHIEVEMENTS), p2)}")
    print(f"Charlie is missing: {set.difference(set(ACHIEVEMENTS), p3)}")
    print(f"Dylan is missing: {set.difference(set(ACHIEVEMENTS), p4)}")


if __name__ == "__main__":
    main()
