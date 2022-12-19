from itertools import combinations
from pprint import pprint

points = set[tuple[int, int, int]]
cubes = set(
    map(
        lambda line: tuple(
            map(
                int,
                line.strip().split(","),
            )
        ),
        open("2022/day_18_input.txt", "r").readlines(),
    )
)


def neighbour_cubes(cube: tuple[int, int, int]) -> set[tuple[int, int, int]]:
    x, y, z = cube
    return {
        (x, y, z + 1),
        (x, y, z - 1),
        (x, y + 1, z),
        (x, y - 1, z),
        (x + 1, y, z),
        (x - 1, y, z),
    }


def part_a_surface_area(
    cube: tuple[int, int, int], cubes: set[tuple[int, int, int]]
) -> int:
    neighbours = neighbour_cubes(cube)
    return 6 - len(cubes & neighbours)


print(sum([part_a_surface_area(cube, cubes) for cube in cubes]))


air_droplets = {
    (x, y, z)
    for x in range(max([coord[0] for coord in cubes]))
    for y in range(max([coord[1] for coord in cubes]))
    for z in range(max([coord[2] for coord in cubes]))
    if part_a_surface_area((x, y, z), cubes) == 0
}


def air_pockets(rocks: set[tuple[int, int, int]]) -> set[tuple[int, int, int]]:
    max_x, max_y, max_z = tuple(
        max([coord[i] for coord in cubes]) + 1 for i in [0, 1, 2]
    )
    possibilities = {
        (x, y, z)
        for x in range(max_x + 1)
        for y in range(max_y + 1)
        for z in range(max_z + 1)
    }
    pockets = set(map(lambda t: frozenset({t}), possibilities - rocks))
    final_pocket = {(max_x, max_y, max_z)}
    merges = 1
    while merges > 0:
        merges = 0
        for pocket in pockets:
            if neighbours(final_pocket, pocket):
                final_pocket |= pocket
                pockets -= pocket
                merges += 1

    pprint(final_pocket)
    return final_pocket


def neighbours(p1: points, p2: points) -> bool:
    # two sets of points are neighbours if any neighbour of any point in p1 is the same as any point in p2
    r = set()
    for point in p1:
        r |= neighbour_cubes(point)
    return bool(r & p2)


def part_b_surface_area(
    cube: tuple[int, int, int], cubes: set[tuple[int, int, int]]
) -> int:
    neighbours = neighbour_cubes(cube)
    return 6 - len((cubes | air_droplets) & neighbours)


# print(sum([part_b_surface_area(cube, cubes) for cube in cubes]))
air_pockets(cubes)
