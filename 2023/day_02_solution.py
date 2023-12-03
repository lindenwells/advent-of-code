MAX_RED, MAX_GREEN, MAX_BLUE = 12, 13, 14


def is_game_eligible(game: str) -> int:
    game_id = int(line.split(": ")[0].split(" ")[1])
    rounds = game.split(": ")[1].split("; ")
    for game_round in rounds:
        reds, greens, blues = [0], [0], [0]
        for dice in game_round.strip().split(", "):
            match dice.split(" "):
                case [number, "red"]:
                    reds.append(int(number))
                case [number, "green"]:
                    greens.append(int(number))
                case [number, "blue"]:
                    blues.append(int(number))
        if max(reds) > MAX_RED or max(greens) > MAX_GREEN or max(blues) > MAX_BLUE:
            return 0
    return game_id


def game_power(game: str) -> int:
    game_id = int(game.split(": ")[0].split(" ")[1])
    rounds = game.split(": ")[1].split("; ")
    reds, greens, blues = [1], [1], [1]
    for game_round in rounds:
        for dice in game_round.strip().split(", "):
            match dice.split(" "):
                case [number, "red"]:
                    reds.append(int(number))
                case [number, "green"]:
                    greens.append(int(number))
                case [number, "blue"]:
                    blues.append(int(number))
    return max(reds) * max(greens) * max(blues)


assert game_power("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == 48
assert (
    game_power("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue") == 12
)
assert (
    game_power(
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    )
    == 1560
)
assert (
    game_power(
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
    )
    == 630
)
assert game_power("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green") == 36


with open("2023/day_02_input.txt") as f:
    sum_of_eligible_game_ids = 0
    for line in f.readlines():
        sum_of_eligible_game_ids += is_game_eligible(line)

    f.seek(0)

    print(sum(game_power(game) for game in f.readlines()))

    print(sum_of_eligible_game_ids)
