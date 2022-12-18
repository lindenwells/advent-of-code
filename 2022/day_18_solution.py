from functools import reduce

cubes = set(
    map(
        lambda line: tuple(
            map(
                int,
                line.strip().split(","),
            )
        ),
        open("day_18_input.txt", "r").readlines(),
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
    possibilities = {
        (x, y, z)
        for x in range(max([coord[0] for coord in cubes]))
        for y in range(max([coord[1] for coord in cubes]))
        for z in range(max([coord[2] for coord in cubes]))
    }
    start = (0, 0, 0)
    return set()  # todo finish


def part_b_surface_area(
    cube: tuple[int, int, int], cubes: set[tuple[int, int, int]]
) -> int:
    neighbours = neighbour_cubes(cube)
    return 6 - len((cubes | air_droplets) & neighbours)


print(sum([part_b_surface_area(cube, cubes) for cube in cubes]))
