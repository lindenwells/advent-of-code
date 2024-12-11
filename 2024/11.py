from get_input import get_input
import itertools
import datetime

from functools import cache


def flatten(list_of_lists):
    return list(itertools.chain.from_iterable(list_of_lists))


@cache
def transform(stone: int) -> list[int]:
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        stone_string = str(stone)
        length = len(stone_string)
        first = stone_string[0 : length // 2]
        second = stone_string[length // 2 :]
        return [int(first), int(second)]
    else:
        return [stone * 2024]


stones = list(map(lambda stone: int(stone), get_input(11)[0].strip().split()))
# stones = [125, 17]


print(stones)

for i in range(25):
    stones = flatten([transform(stone) for stone in stones])
    # print(stones)
    print(i, datetime.datetime.now(), len(stones))


print(len(stones))
