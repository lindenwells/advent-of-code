from functools import reduce
from itertools import repeat
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


def zip_longest(*args, fillvalue=None):
    # zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
    iterators = [iter(it) for it in args]
    num_active = len(iterators)
    if not num_active:
        return
    while True:
        values = []
        for i, it in enumerate(iterators):
            try:
                value = next(it)
            except StopIteration:
                num_active -= 1
                if not num_active:
                    return
                if i == 0:
                    iterators[i] = repeat(fillvalue)
                    value = fillvalue
            values.append(value)
        yield tuple(values)


def ordered(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x < y
    elif isinstance(x, list) and isinstance(y, list):
        # if len(x) > 0:
        #     if len(y) > 0:
        #         return reduce(lambda a, b: a and ordered(b[0], b[1]), zip(x, y), True)
        #     else:
        #         return False
        # else:
        #     if len(y) > 0:
        #         return True
        #     else:
        #         return True  # ?
        # for index, value in enumerate(x):
        # if index > len(y):

        if x == [] and y != []:
            return True
        elif y == [] and x != []:
            return False
        else:
            if isinstance(x[0], int) and isinstance(y[0], int):
                return x < y
            elif isinstance(x[0], int) and isinstance(y[0], list):
                return ordered([x[0]], y[0])
            elif isinstance(x[0], list) and isinstance(y[0], int):
                return ordered(x[0], [y[0]])
            elif isinstance(x[0], list) and isinstance(y[0], list):
                return ordered(x[0], y[0])
            elif x[0] == y[0]:
                return ordered(x[1:], y[1:])
            else:
                return False

    elif isinstance(x, int) and isinstance(y, list):
        return ordered([x], y)
    elif isinstance(x, list) and isinstance(y, int):
        return ordered(x, [y])


print([ordered(first, second) for index, (first, second) in enumerate(pairs)])
