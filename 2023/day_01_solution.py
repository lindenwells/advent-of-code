from string import ascii_lowercase, ascii_uppercase
digit_words = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}

def get_number_from_line(line: str) -> int:
    stripped = line.strip().lstrip(ascii_uppercase).lstrip(ascii_lowercase).rstrip(ascii_uppercase).rstrip(ascii_lowercase)
    return int(stripped[0] + stripped[-1]) if len(stripped) > 0 else 0

with open("day_01_input.txt") as f:
    print(sum(map(get_number_from_line, f.readlines())))