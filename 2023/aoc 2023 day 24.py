from dataclasses import dataclass
from itertools import combinations
from math import inf


@dataclass
class Line:
    x: int
    y: int
    dx: int
    dy: int
    gradient: float
    y_intercept: float  # y - gradient * x


def intersect(l1: Line, l2: Line) -> tuple[int, int] | None:
    if l1.gradient == l2.gradient:
        return None
    return (
        (l2.y_intercept - l1.y_intercept) / (l1.gradient - l2.gradient),
        l1.gradient * (l2.y_intercept - l1.y_intercept) / (l1.gradient - l2.gradient),
    )

def parse_line(line: str) -> Line:
    points, velocities = line.split(" @ ")
    x, y, _ = points.split(", ")
    dx, dy, _ = velocities.split(", ")
    x, y = int(x), int(y)
    dx, dy = int(dx), int(dy)
    gradient = inf if -1e-9 <= dx <= 1e-9 else dy / dx

    return Line(x, y, dx, dy, gradient, y - gradient * x)

def main():
    lines = []
    # with open("aoc 2023 day 24 input", "r") as f:
        # lines = f.readlines()
    lines =  """
    19, 13, 30 @ -2,  1, -2
    18, 19, 22 @ -1, -1, -2
    20, 25, 34 @ -2, -2, -4
    12, 31, 28 @ -1, -2, -1
    20, 19, 15 @  1, -5, -3
    """

    lines = list(map(parse_line, lines.splitlines()))
    count = 0
    for l1, l2 in combinations(lines, 2):
        if (point := intersect(l1, l2)) is not None:
            if 200000000000000 <= point[0] <= 400000000000000 and 200000000000000 <= point[1] <= 400000000000000:
                count += 1
    print(count)


if __name__ == "__main__":
    main()
# dx, dy
#  3,  5
#  5 / 3
