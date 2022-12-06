import os

ASCII_DIFF_LOWER = 96
ASCII_DIFF_UPPER = 38

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, "input.txt"), "r") as input:
    sum = 0
    for line in input:
        items_per_sack = int(len(line) / 2)
        first_sack = [*line[:items_per_sack]]
        second_sack = [*line[items_per_sack:-1]]

        common = set(first_sack).intersection(set(second_sack)).pop()
        value = (
            ord(common) - ASCII_DIFF_LOWER
            if common.islower()
            else ord(common) - ASCII_DIFF_UPPER
        )

        sum += value

        # print("a", ord("a"), ord("a") - ASCII_DIFF_LOWER)
        # print("z", ord("z"), ord("z") - ASCII_DIFF_LOWER)

        # print("A", ord("A"), ord("A") - ASCII_DIFF_UPPER)
        # print("Z", ord("Z"), ord("Z") - ASCII_DIFF_UPPER)

    print("Solution Part 1", sum)

with open(os.path.join(__location__, "input.txt"), "r") as input:
    groups = []
    subgroup = []
    line_number = 0
    sum = 0
    for line in input:
        line_number += 1
        subgroup.append([*line[:-1]])

        if line_number % 3 == 0:
            groups.append(subgroup)
            subgroup = []

    sum = 0
    for group in groups:
        sub1 = group[0]
        sub2 = group[1]
        sub3 = group[2]

        common = set(sub1).intersection(sub2, sub3).pop()
        value = (
            ord(common) - ASCII_DIFF_LOWER
            if common.islower()
            else ord(common) - ASCII_DIFF_UPPER
        )

        sum += value

    print("Solution Part 2", sum)
