from get_input import get_input
from itertools import groupby

input_stuff = groupby(get_input(day=25), lambda line: line.strip() == '')

lock_and_keys = []
for key, group in input_stuff:
    if key == False:
        lock_and_keys.append(list(group))

locks = []
keys = []

def transpose(line: list[str]) -> list[str]:
    return ["".join([row[i] for row in line]) for i in range(len(line[0]))]

assert transpose(['#####', '#####', '###.#', '##..#', '##..#', '#....', '.....']) == ['######.', '#####..', '###....', '##.....', '#####..']


for lock_or_key in lock_and_keys:
    if all([char == "#" for char in lock_or_key[0]]):
        locks.append(lock_or_key)
    else:
        keys.append(lock_or_key)

def lock_height(lock: list[str]) -> list[int]:
    return [barrel.count('#') for barrel in transpose(lock[1:])]
assert lock_height(['#####', '#####', '#####', '#.##.', '...#.', '.....', '.....']) == [3, 2, 3, 4, 2]

"""Key height is equivalent to the lock height if the rows are reversed."""
def key_height(key: list[str]) -> list[int]:
    return lock_height(list(reversed(key)))
assert key_height(['.....', '.#.#.', '.###.', '.###.', '.###.', '.####', '#####']) == [0, 5, 4, 5, 1]

num_compatible_combos = 0
for key in keys:
    for lock in locks:
        if not any([l_h + k_h > 5 for l_h, k_h in zip(lock_height(lock), key_height(key))]):
            num_compatible_combos += 1

print(num_compatible_combos)
