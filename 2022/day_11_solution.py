from dataclasses import dataclass

@dataclass
class Monkey:
    number: int
    starting_items: list
    operation: callable
    test: callable

monkeys = []
monkey = Monkey(69, [], lambda x: x, lambda x: x)
for line in open('day_11_input.txt', 'r'):
    line = line.strip()
    if line.startswith('Monkey'):
        monkeys.append(monkey)
        monkey = Monkey(number=int(line.split(" ")[1].rstrip(":\n")), starting_items=[], operation=lambda x: x, test=lambda x: x)
    elif line.startswith('Starting'):
        items = list(map(int, line.split(":")[1].strip().split(", ")))
        monkey.starting_items = items
    elif line.startswith('Operation'):
        [exp1, operator, exp2] = line.split('=')[1].strip().split(' ')
        assert exp1 == "old" # assuming the first one is always old
        if operator == "+":
            if exp2 == "old":
                return lambda old: old + old
            else:
                return lambda old: old + int(exp2)
        elif operator == "*":
            if exp2 == "old":
                return lambda old: old * old
            else:
                return lambda old: old * int(exp2)
        else:
            assert False, "why are we here"
    elif line.startswith('Test'

#print(monkeys)
