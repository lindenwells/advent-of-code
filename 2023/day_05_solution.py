from get_input import get_input
from collections import defaultdict

puzzle_input = get_input(2023, 5)


class CustomDict(defaultdict):
    def __missing__(self, __key):
        return __key


def parse(line: str, mapping: dict[str, dict[int, int]], step: str) -> None:
    dest_range_start, src_range_start, range_length = list(map(int, line.split(" ")))
    for i in range(range_length):
        mapping[src_range_start + i] = dest_range_start + i


def parse_seeds_line(line: str) -> set[int]:
    return set(map(int, line.split(": ")[1].split(" ")))


steps = [
    "seeds",
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]

step_index = 0
mappings = {step_name: CustomDict() for step_name in steps}
seeds = set()

for line in puzzle_input:
    if line.startswith("seeds: "):
        seeds = parse_seeds_line(line)
    elif line.endswith(" map:\n"):
        step_index += 1
    elif line == "\n":
        continue
    else:
        parse(line, mappings, steps[step_index])


pass
