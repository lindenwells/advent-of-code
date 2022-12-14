import json

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


print(
    sum(
        [
            index + 1 if compare(first, second) == -1 else 0
            for (index, (first, second)) in enumerate(pairs)
        ]
    )
)
