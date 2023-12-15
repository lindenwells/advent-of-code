from get_input import get_input

stuff = get_input(2023, 15)

line = stuff[0]

def compute_hash(string: str) -> int:
    value = 0
    for character in string:
        value += ord(character)
        value *= 17
        value %= 256
    return value

print(sum(map(compute_hash, line.strip().split(","))))