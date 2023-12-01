from string import ascii_lowercase, ascii_uppercase
from collections import defaultdict

digit_words = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

bruh = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}


def get_number_from_line(line: str) -> int:
    stripped = line.strip().lstrip(ascii_lowercase).rstrip(ascii_lowercase)
    return int(stripped[0] + stripped[-1]) if len(stripped) > 0 else 0


def smallest(digit_word: str, digit) -> str:
    digit_words[digit_word]


def get_number_from_line_2(line: str) -> int:
    digit_counts = {}
    stripped = line.strip().lstrip(ascii_lowercase).rstrip(ascii_lowercase)

    for digit_word in digit_words.keys():
        start = 0
        while True:
            try:
                index_of_digit_word = line.index(digit_word, start)
                digit_counts[index_of_digit_word] = digit_word
                start += len(digit_word) + index_of_digit_word
            except ValueError:
                break

    for digit_word in digit_words.values():

        start = 0
        while True:
            try:
                index_of_digit_word = line.index(digit_word, start)
                digit_counts[index_of_digit_word] = bruh[int(digit_word)]
                start += len(digit_word) + index_of_digit_word
            except ValueError:
                break
    if digit_counts:
        result = int(
            digit_words[digit_counts[min(digit_counts.keys())]]
            + digit_words[digit_counts[max(digit_counts.keys())]]
        )
        return result
    else:
        print(line)


assert get_number_from_line("1abc2") == 12
assert get_number_from_line("pqr3stu8vwx") == 38
assert get_number_from_line("a1b2c3d4e5f") == 15
assert get_number_from_line("treb7uchet") == 77

assert get_number_from_line_2("two1nine") == 29
assert get_number_from_line_2("eightwothree") == 83
assert get_number_from_line_2("abcone2threexyz") == 13
assert get_number_from_line_2("xtwone3four") == 24
assert get_number_from_line_2("4nineeightseven2") == 42
assert get_number_from_line_2("zoneight234") == 14
assert get_number_from_line_2("7pqrstsixteen") == 76
assert get_number_from_line_2("1ight") == 11

with open("2023/day_01_input.txt") as f:
    print(sum(map(get_number_from_line, f.readlines())))

    f.seek(0)
    print(sum(map(get_number_from_line_2, f.readlines())))
