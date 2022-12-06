import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, "input.txt"), "r") as input:
    count = 0
    for line in input:
        a1, a2 = line.split(",")

        a1_1, a1_2 = a1.split("-")
        a2_1, a2_2 = a2.split("-")

        if (int(a1_1) <= int(a2_1) and int(a1_2) >= int(a2_2)) or (
            int(a2_1) <= int(a1_1) and int(a2_2) >= int(a1_2)
        ):
            count += 1

    print("Solution Part 1", count)

with open(os.path.join(__location__, "input.txt"), "r") as input:
    count = 0
    for line in input:
        a1, a2 = line.split(",")

        a1_1, a1_2 = a1.split("-")
        a2_1, a2_2 = a2.split("-")

        range_1 = list(range(int(a1_1), int(a1_2) + 1))
        range_2 = list(range(int(a2_1), int(a2_2) + 1))
        intersection = set(range_1).intersection(range_2)
        if intersection:
            count += 1

    print("Solution Part 2", count)
