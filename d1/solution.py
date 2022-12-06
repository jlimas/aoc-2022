import os
from collections import defaultdict

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, "input.txt"), "r") as input:
    elfs = defaultdict(int)
    elf_number = 1

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
