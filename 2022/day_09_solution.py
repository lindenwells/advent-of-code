from operator import sub

UP = "U"
DOWN = "D"
RIGHT = "R"
LEFT = "L"

get_move_func = {
    UP: lambda position, d: (position[0] + d, position[1]),
    DOWN: lambda position, d: (position[0] - d, position[1]),
    RIGHT: lambda position, d: (position[0], position[1] + d),
    LEFT: lambda position, d: (position[0], position[1] - d),
}


def move_tail(
    head_position: tuple[int, int], tail_position: tuple[int, int]
) -> tuple[int, int]:
    if (
        abs(head_position[0] - tail_position[0]) <= 1
        and abs(head_position[1] - tail_position[1]) <= 1
    ):
        # do nothing since the tail is already touching the head
        return tail_position
    if head_position[0] == tail_position[0] or head_position[1] == tail_position[1]:
        if head_position[0] - tail_position[0] == 2:
            # move up
            return (tail_position[0] + 1, tail_position[1])
        elif tail_position[0] - head_position[0] == 2:
            # move down
            return (tail_position[0] - 1, tail_position[1])
        elif head_position[1] - tail_position[1] == 2:
            # move right
            return (tail_position[0], tail_position[1] + 1)
        elif tail_position[1] - head_position[1] == 2:
            # move left
            return (tail_position[0], tail_position[1] - 1)
    else:
        difference = tuple(map(sub, head_position, tail_position))
        if difference[0] > 0 and difference[1] > 0:
            # move diagonally to the top right
            return (tail_position[0] + 1, tail_position[1] + 1)
        elif difference[0] > 0 and difference[1] < 1:
            # move diagonally to the top left
            return (tail_position[0] + 1, tail_position[1] - 1)
        elif difference[0] < 0 and difference[1] > 0:
            # move diagonally to the bottom right
            return (tail_position[0] - 1, tail_position[1] + 1)
        elif difference[0] < 0 and difference[1] < 0:
            # move diagonally to the bottom left
            return (tail_position[0] - 1, tail_position[1] - 1)


def part_a():
    moves = list(
        map(
            lambda line: line.strip().split(" "),
            open("2022/day_09_example_input.txt", "r").readlines(),
        )
    )
    for move in moves:
        [direction, distance] = move
        move[1] = int(distance)

    visited = {(0, 0)}  # start at the bottom left
    head_position = (0, 0)
    tail_position = (0, 0)

    for direction, distance in moves:
        for _ in range(distance):
            head_position = get_move_func[direction](head_position, 1)
            tail_position = move_tail(head_position, tail_position)

            visited.add(tail_position)

    print(len(visited))


def part_b():
    moves = list(
        map(
            lambda line: line.strip().split(" "),
            open("2022/day_09_input.txt", "r").readlines(),
        )
    )
    for move in moves:
        [direction, distance] = move
        move[1] = int(distance)
    START = (0, 0)

    knot_positions = [START] * 10  # 0 is the head, 1-9 are the knots
    visited = {START}
    for direction, distance in moves:
        for _ in range(distance):
            knot_positions[0] = get_move_func[direction](knot_positions[0], 1)
            # the below code is a bit trash. I like the commented-out code below better, but it's off by one.
            for i, position in enumerate(knot_positions[1:]):
                knot_positions[i + 1] = move_tail(knot_positions[i], position)
            # knot_positions = [knot_positions[0]] + [
            #     move_tail(leader, follower)
            #     for leader, follower in zip(knot_positions, knot_positions[1:])
            # ]

            visited.add(knot_positions[-1])
    print(len(visited))


def main():
    part_a()
    part_b()


if __name__ == "__main__":
    main()
