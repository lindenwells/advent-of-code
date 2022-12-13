import json
from pprint import pprint

# pairs = [
#     (first, second)
#     for first, second in open("day_13_input.txt", "r").read().split("\n\n\n")
# ]

pairs = list(
    map(
        lambda twolines: tuple(
            map(lambda line: json.loads(line), twolines.splitlines())
        ),
        open("day_13_example_input.txt", "r").read().split("\n\n"),
    )
)


def ordered(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x < y
    elif isinstance(x, list) and isinstance(y, list):
        return any([ordered(a, b) for a, b in zip(x, y)])
    elif isinstance(x, int) and isinstance(y, list):
        return ordered([x], y)
    elif isinstance(x, list) and isinstance(y, int):
        return ordered(x, [y])


print([ordered(first, second) for index, (first, second) in enumerate(pairs)])
print(len(list(pairs)))
