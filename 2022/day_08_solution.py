grid = list(
    map(
        lambda line: [int(c) for c in line.strip()],
        open("day_08_input.txt", "r").readlines(),
    )
)

# region part a
def is_visible(grid: list[list[int]], row: int, column: int) -> bool:

    value = grid[row][column]
    if row in {0, len(grid) - 1} or column in {0, len(grid[0]) - 1}:
        # it's on the edge, so it's visible
        return True

    if value > max(grid[row][:column] or [-99]) or value > max(
        grid[row][column + 1 :] or [-99]
    ):
        return True

    transposed_grid = [list(sublist) for sublist in list(zip(*grid))]
    if value > max(transposed_grid[column][:row] or [-99]) or value > max(
        transposed_grid[column][row + 1 :] or [-99]
    ):
        return True

    return False


print(
    sum(
        [
            int(is_visible(grid, row, column))
            for row in range(len(grid))
            for column in range(len(grid[0]))
        ]
    )
)
# endregion

# region part b
def scenic_score(grid: list[list[int]], row: int, column: int) -> int:

    value = grid[row][column]
    left, right, up, down = 0, 0, 0, 0
    if row in {0, len(grid) - 1} or column in {0, len(grid[0]) - 1}:
        # it's on the edge, so the product will be zero
        return 0

    if value > max(grid[row][:column] or [-99]) or value > max(
        grid[row][column + 1 :] or [-99]
    ):
        return True

    transposed_grid = [list(sublist) for sublist in list(zip(*grid))]
    if value > max(transposed_grid[column][:row] or [-99]) or value > max(
        transposed_grid[column][row + 1 :] or [-99]
    ):
        return True

    return False


print(
    sum(
        [
            int(is_visible(grid, row, column))
            for row in range(len(grid))
            for column in range(len(grid[0]))
        ]
    )
)
# endregion
