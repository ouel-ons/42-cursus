"""Exercise 2 - Position Tracker."""

import sys
import math


def create_position(x: int, y: int, z: int) -> tuple[int, int, int]:
    """Create a 3D position tuple."""
    return (x, y, z)


def distance_3d(
    a: tuple[int, int, int],
    b: tuple[int, int, int],
) -> float:
    """Compute Euclidean distance between two 3D points."""
    x1, y1, z1 = a
    x2, y2, z2 = b
    return math.sqrt(
        (x2 - x1) ** 2
        + (y2 - y1) ** 2
        + (z2 - z1) ** 2
    )


def parse_coordinates(coord_str: str) -> tuple[int, int, int]:
    """Parse 'x,y,z' into a tuple of ints."""
    parts: list[str] = coord_str.split(",")
    x: int = int(parts[0])
    y: int = int(parts[1])
    z: int = int(parts[2])
    return (x, y, z)


def main() -> None:
    print("=== Game Coordinate System ===")
    print()
    origin: tuple[int, int, int] = create_position(0, 0, 0)

    if len(sys.argv) == 3:
        try:
            a: tuple[int, int, int] = parse_coordinates(sys.argv[1])
            b: tuple[int, int, int] = parse_coordinates(sys.argv[2])
            print('Parsing coordinates:', '"' + sys.argv[1] + '"')
            print("Parsed position:", a)
            print('Parsing coordinates:', '"' + sys.argv[2] + '"')
            print("Parsed position:", b)
            print(
                "Distance between",
                a,
                "and",
                b,
                ":",
                distance_3d(a, b),
            )
        except ValueError as e:
            print("Error parsing coordinates:", e)
            print("Error details - Type:", type(e).__name__, ", Args:", e.args)
        return

    pos: tuple[int, int, int] = create_position(10, 20, 5)
    print("Position created:", pos)
    print(
        "Distance between",
        origin,
        "and",
        pos,
        ":",
        distance_3d(origin, pos),
    )
    print()
    coord_text: str = "3,4,0"
    print('Parsing coordinates:', '"' + coord_text + '"')
    parsed: tuple[int, int, int] = parse_coordinates(coord_text)
    print("Parsed position:", parsed)
    print(
        "Distance between",
        origin,
        "and",
        parsed,
        ":",
        distance_3d(origin, parsed),
    )
    print()
    bad_text: str = "abc,def,ghi"
    print('Parsing invalid coordinates:', '"' + bad_text + '"')
    try:
        _ = parse_coordinates(bad_text)
    except ValueError as e:
        print("Error parsing coordinates:", e)
        print("Error details - Type:", type(e).__name__, ", Args:", e.args)
    print()
    print("Unpacking demonstration:")
    x, y, z = parsed
    print("Player at x=", x, ", y=", y, ", z=", z, sep="")
    print("Coordinates: X=", x, ", Y=", y, ", Z=", z, sep="")


if __name__ == "__main__":
    main()
