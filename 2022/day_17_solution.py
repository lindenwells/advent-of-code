from itertools import repeat, cycle

R = '#'  # rock
E = '.'  # empty

ROCKS = [
    [[R, R, R, R]],
    [[E, R, E], [R, R, R], [E, R, E]],
    [[E, E, R], [E, E, R], [R, R, R]],
    [[R], [R], [R], [R]]
    [[R, R], [R, R]]
]

grid = [[]]
moving_rock = set()

jet_directions = open("day_17_input.txt", 'r').read().strip()

for _ in cycle(ROCKS):
    
    drop_rock(jet_directions, grid)