from itertools import groupby

def process_command(command: str, current_directory: list[str], tree: dict):
    command = command.strip()
    if command.startswith

def process_output(output: str, tree: dict):
    pass

def process_line(line: str, current_directory: list[str], tree: dict):
    if line.startswith("$"):
        process_command(line.removeprefix("$"))
    else:
        process_output(line, tree)

def main():
    tree = {}
    commands = []
    accumulated_command = []
    current_directory = ["/"]
    for command in list(
        map(lambda line: line.strip(), open("day_07_input.txt", "r").readlines())
    ):
        if command.startswith("$"):
            commands.append(accumulated_command)
            accumulated_command = []
        else:
            accumulated_command.append(command)


if __name__ == "__main__":
    main()
