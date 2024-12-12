from get_input import get_input
import itertools

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


evolved_stones = stones
for i in range(25):
    evolved_stones = flatten([transform(stone) for stone in evolved_stones])

print("Part 1", len(evolved_stones))


@cache
def expansions_from_stone(stone: int, count: int) -> int:
    # print(f"expansions_from_stone({stone}, {count})")
    if count == 0:
        return 1

    if stone == 0:
        return expansions_from_stone(1, count - 1)

    stone_string = str(stone)
    if len(stone_string) % 2 == 0:
        length = len(stone_string)
        first = stone_string[0 : length // 2]
        second = stone_string[length // 2 :]
        return expansions_from_stone(int(first), count - 1) + expansions_from_stone(
            int(second), count - 1
        )

    return expansions_from_stone(stone * 2024, count - 1)


# print("Part 1", sum(expansions_from_stone(stone, 25) for stone in stones))
print("Part 2", sum(expansions_from_stone(stone, 75) for stone in stones))
