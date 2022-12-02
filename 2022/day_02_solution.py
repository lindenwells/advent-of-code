ROCK = "X"
PAPER = "Y"
SCISSORS = "Z"

shape_scores = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
}

game_outcome = {
    ("A", "X"): 3,
    ("A", "Y"): 6,
    ("A", "Z"): 0,
    ("B", "X"): 0,
    ("B", "Y"): 3,
    ("B", "Z"): 6,
    ("C", "X"): 6,
    ("C", "Y"): 0,
    ("C", "Z"): 3,
}


def score_game(opponent: str, you: str) -> int:
    return game_outcome[(opponent, you)] + shape_scores[you]


total = sum(
    map(
        lambda moves: score_game(moves[0], moves[1]),
        map(
            lambda line: line.strip().split(" "),
            open("day_02_input.txt", "r").readlines(),
        ),
    )
)

print(total)


choose_move = {
    ("A", "X"): SCISSORS,
    ("A", "Y"): ROCK,
    ("A", "Z"): PAPER,
    ("B", "X"): ROCK,
    ("B", "Y"): PAPER,
    ("B", "Z"): SCISSORS,
    ("C", "X"): PAPER,
    ("C", "Y"): SCISSORS,
    ("C", "Z"): ROCK,
}

total = sum(
    map(
        lambda moves: score_game(moves[0], choose_move[(moves[0], moves[1])]),
        map(
            lambda line: line.strip().split(" "),
            open("day_02_input.txt", "r").readlines(),
        ),
    )
)
print(total)
