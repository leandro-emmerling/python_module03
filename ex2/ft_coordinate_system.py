#!/usr/bin/env python3


import math


def get_player_pos() -> tuple[float, float, float]:
    """Validate the input and return the tuple with the Coordinates."""
    while True:
        raw: str = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts: list[str] = raw.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        try:
            return (float(parts[0]), float(parts[1]), float(parts[2]))
        except ValueError:
            for part in parts:
                try:
                    float(part)
                except ValueError as e:
                    print(f"Error on parameter '{part}': {e}")


def calc_distance(pos1: tuple[float, float, float],
                  pos2: tuple[float, float, float]) -> float:
    """Calculate the distance between two given 3D points."""
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return (math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))


def main() -> None:
    """Run the main program."""
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    pos1: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    print(f"Distance to center: "
          f"{round(calc_distance(pos1, (0.0, 0.0, 0.0)), 4)}")
    print("\nGet a second set of coordinates")
    pos2: tuple[float, float, float] = get_player_pos()
    print(f"Distance between the 2 sets of coordinates: "
          f"{round(calc_distance(pos1, pos2), 4)}")


if __name__ == "__main__":
    main()
