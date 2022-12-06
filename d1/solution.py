from collections import defaultdict

elfs = defaultdict(int)
elf_number = 1

with open("input.txt", "r") as input:
    for line in input:
        if line != "\n":
            elfs[elf_number] += int(line)
        else:
            elf_number += 1

    sorted_elfs = sorted(elfs.items(), key=lambda x: x[1], reverse=True)

    # Part 1
    print("Top 1", sorted_elfs[0][1])

    # Part 2
    print("Top 3", sorted_elfs[0][1] + sorted_elfs[1][1] + sorted_elfs[2][1])
