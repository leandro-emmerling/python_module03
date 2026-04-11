#!/usr/bin/env python3


import sys


def parse_inventory() -> dict[str, int]:
    """Validate the Input and return the dictionary"""
    inv: dict[str, int] = {}
    for arg in sys.argv[1:]:
        parts: list[str] = arg.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        try:
            int(parts[1])
        except ValueError as e:
            print(f"Quantity error for '{parts[0]}': {e}")
            continue
        if parts[0] in inv:
            print(f"Redundant item '{parts[0]}' - discarding")
            continue
        inv[parts[0]] = int(parts[1])
    return (inv)


def get_max_item(inv: dict[str, int]) -> str:
    """Return the key with the highest value."""
    max_item: str = list(inv.keys())[0]
    for item in inv.keys():
        if inv[item] > inv[max_item]:
            max_item = item
    return max_item


def get_min_item(inv: dict[str, int]) -> str:
    """Return the key with the highest value."""
    min_item: str = list(inv.keys())[0]
    for item in inv.keys():
        if inv[item] < inv[min_item]:
            min_item = item
    return min_item


def display_stats(inv: dict[str, int]) -> None:
    """Display all stats from the passed inventory items."""
    if not inv:
        print("Your inventory is empty, noob!")
        return
    print(f"Got inventory: {inv}")
    print(f"Item list: {list(inv.keys())}")
    print(f"Total quantity of the {len(inv)} items: {sum(inv.values())}")
    for item in inv.keys():
        print(f"Item {item} represents "
              f"{round(inv[item] / sum(inv.values()) * 100, 1)}%")
    print(f"Item most abundant: {get_max_item(inv)} "
          f"with quantity {inv[get_max_item(inv)]}")
    print(f"Item least abundant: {get_min_item(inv)} "
          f"with quantity {inv[get_min_item(inv)]}")
    inv.update({"magic_item": 1})
    print(f"Updated inventory: {inv}")


def main() -> None:
    """Run the main Program."""
    print("=== Inventory System Analysis ===")
    display_stats(parse_inventory())


if __name__ == "__main__":
    main()
