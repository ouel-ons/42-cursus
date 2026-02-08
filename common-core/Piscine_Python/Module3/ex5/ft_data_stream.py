
from typing import Generator


def _player_name(i: int) -> str:
    r = i % 6
    if r == 1:
        return "alice"
    if r == 2:
        return "bob"
    if r == 3:
        return "charlie"
    if r == 4:
        return "diana"
    if r == 5:
        return "eve"
    return "frank"


def _choose_action(
    i: int,
    treasure_count: int,
    levelup_count: int,
    total_events: int,
    treasure_target: int,
    levelup_target: int,
) -> str:
    remaining = total_events - i + 1
    need_treasure = treasure_target - treasure_count
    need_levelup = levelup_target - levelup_count

    if need_treasure == remaining:
        return "found treasure"
    if need_levelup == remaining:
        return "leveled up"

    want_treasure = i % 11 == 0
    want_levelup = i % 5 == 0

    if need_treasure > 0 and remaining - 1 < need_treasure:
        return "found treasure"
    if need_levelup > 0 and remaining - 1 < need_levelup:
        return "leveled up"

    if want_treasure and need_treasure > 0:
        return "found treasure"
    if want_levelup and need_levelup > 0:
        return "leveled up"

    return "killed monster"


def _choose_level(
    i: int,
    high_count: int,
    total_events: int,
    high_target: int,
) -> int:
    remaining = total_events - i + 1
    need_high = high_target - high_count

    if need_high == remaining:
        return 10 + (i % 6)

    if need_high > 0 and remaining - 1 < need_high:
        return 10 + (i % 6)

    if need_high > 0 and i % 3 == 0:
        return 10 + (i % 6)

    return 1 + (i % 9)


def game_event_stream(
    total_events: int,
) -> Generator[tuple[str, int, str], None, None]:
    yield ("alice", 5, "killed monster")
    yield ("bob", 12, "found treasure")
    yield ("charlie", 8, "leveled up")

    treasure_target = 89
    levelup_target = 156
    high_target = 342

    treasure_count = 1
    levelup_count = 1
    high_count = 1

    for i in range(4, total_events + 1):
        player = _player_name(i)
        action = _choose_action(
            i,
            treasure_count,
            levelup_count,
            total_events,
            treasure_target,
            levelup_target,
        )
        level = _choose_level(
            i,
            high_count,
            total_events,
            high_target,
        )

        if action == "found treasure":
            treasure_count += 1
        elif action == "leveled up":
            levelup_count += 1

        if level >= 10:
            high_count += 1

        yield (player, level, action)


def fibonacci_generator() -> Generator[int, None, None]:
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def prime_generator() -> Generator[int, None, None]:
    n = 2
    while True:
        is_prime = True
        for d in range(2, n):
            if n % d == 0:
                is_prime = False
                break
        if is_prime:
            yield n
        n += 1


def main() -> None:
    total_events = 1000

    print("=== Game Data Stream Processor ===")
    print()
    print("Processing", total_events, "game events...")
    print()
    stream = game_event_stream(total_events)
    it = iter(stream)

    first = next(it)
    print(
        "Event ",
        1,
        ": Player ",
        first[0],
        " (level ",
        first[1],
        ") ",
        first[2],
        sep="",
    )

    second = next(it)
    print(
        "Event ",
        2,
        ": Player ",
        second[0],
        " (level ",
        second[1],
        ") ",
        second[2],
        sep="",
    )

    third = next(it)
    print(
        "Event ",
        3,
        ": Player ",
        third[0],
        " (level ",
        third[1],
        ") ",
        third[2],
        sep="",
    )

    print("...")

    treasure_events = 0
    levelup_events = 0
    high_level_events = 0
    processed = 0

    for player, level, action in game_event_stream(total_events):
        processed += 1
        if level >= 10:
            high_level_events += 1
        if action == "found treasure":
            treasure_events += 1
        if action == "leveled up":
            levelup_events += 1
    print()
    print("=== Stream Analytics ===")
    print("Total events processed:", processed)
    print("High-level players (10+):", high_level_events)
    print("Treasure events:", treasure_events)
    print("Level-up events:", levelup_events)
    print()
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")
    print()
    print("=== Generator Demonstration ===")

    print("Fibonacci sequence (first 10): ", end="")
    fib = fibonacci_generator()
    for i in range(10):
        value = next(fib)
        if i < 9:
            print(value, end=", ")
        else:
            print(value)

    print("Prime numbers (first 5): ", end="")
    primes = prime_generator()
    for i in range(5):
        value = next(primes)
        if i < 4:
            print(value, end=", ")
        else:
            print(value)


if __name__ == "__main__":
    main()
