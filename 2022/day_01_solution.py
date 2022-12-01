with open("day_1_input.txt", "r") as f:
    elf_calories = [0]
    for line in f:
        g = line.strip()
        if g == "":
            elf_calories.append(0)
        else:
            elf_calories[-1] += int(g)

    print(max(elf_calories))

with open("day_1_input.txt", "r") as f:
    elf_calories = [0]
    for line in f:
        g = line.strip()
        if g == "":
            elf_calories.append(0)
        else:
            elf_calories[-1] += int(g)

    print(sum(sorted(elf_calories)[-3:]))
