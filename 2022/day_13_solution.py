import json
from itertools import chain
from functools import cmp_to_key
from pprint import pprint

pairs = list(
    map(
        lambda twolines: tuple(
            map(lambda line: json.loads(line), twolines.splitlines())
        ),
        open("day_13_input.txt", "r").read().split("\n\n"),
    )
)


def compare(x, y) -> int:
    if isinstance(x, int) and isinstance(y, int):
        if x == y:
            return 0
        elif x < y:
            return -1
        else:
            return 1

    elif isinstance(x, list) and isinstance(y, list):
        i = 0

        while i < len(x) and i < len(y):
            if (c := compare(x[i], y[i])) != 0:
                return c
            i += 1

        if i == len(x) and i < len(y):
            return -1
        elif i < len(x) and i == len(y):
            return 1
        else:
            return 0

    elif isinstance(x, int) and isinstance(y, list):
        return compare([x], y)
    elif isinstance(x, list) and isinstance(y, int):
        return compare(x, [y])


def part_a():
    print(
        sum(
            [
                index + 1 if compare(first, second) == -1 else 0
                for (index, (first, second)) in enumerate(pairs)
            ]
        )
    )


def part_b():
    packets = list(chain(*pairs, [[2]], [[2]]))
    packets.append([[2]])
    packets.append([[6]])
    sorted_packets = sorted(packets, key=cmp_to_key(lambda x, y: compare(x, y)))
    print((sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1))


part_a()
part_b()
