#!/usr/bin/env python3


import typing
import random


PLAYERS: list[str] = [
    "alice", "bob", "charlie", "dylan"
]

ACTIONS: list[str] = [
    "eat", "run", "grab", "move", "swim",
    "climb", "sleep", "release"
]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    """Endless generator for tuple (name, action)."""
    while (True):
        name: str = random.choice(PLAYERS)
        action: str = random.choice(ACTIONS)
        yield (name, action)


def consume_event(
    events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    """Takes list of events and remove one element until it is empty."""
    while (len(events) > 0):
        event = random.choice(events)
        events.remove(event)
        yield event


def main() -> None:
    """Run the main Program."""
    print("=== Game Data Stream Processor ===")
    event_gen = gen_event()
    for i in range(1000):
        event = next(event_gen)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    ten_list: list[tuple[str, str]] = []
    for i in range(10):
        ten_list.append(next(event_gen))
    print(f"Build list of 10 events: {ten_list}")
    for event in consume_event(ten_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_list}")


if __name__ == "__main__":
    main()
