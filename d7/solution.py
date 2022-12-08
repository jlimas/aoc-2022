import os
import re
from collections import defaultdict


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, "input.txt"), "r") as file_input:
    directories = defaultdict(int)
    cwd = []

    for line in file_input:
        if line.startswith("$ cd"):
            prompt, command, directory = line.split()
            if directory == "/":
                cwd.clear()
            elif directory == "..":
                cwd.pop()
            else:
                cwd.append(directory)
            continue

        if re.match(r"\d+", line):
            size, filename = line.split()
            directories["/".join(cwd)] += int(size)

        if line.startswith("dir"):
            subdirectory = line.split()[1]
            directories["/".join(cwd + [subdirectory])] = 0

    def get_nested_dirs_total_size(_path):
        total_size = 0
        for _dir, _size in directories.items():
            if _dir.startswith(_path):
                total_size += _size
        return total_size

    solution_part_1 = 0
    for directory in directories.keys():
        size = get_nested_dirs_total_size(directory)
        if size < 100000:
            solution_part_1 += size

    print("Solution Part 1", solution_part_1)

    solutions = {}
    used_space = get_nested_dirs_total_size("")
    total_space = 70_000_000
    free_space = total_space - used_space

    for directory in directories.keys():
        size = get_nested_dirs_total_size(directory)
        if free_space + size >= 30_000_000:
            solutions[directory] = size
    deletable_spaces = list(solutions.values())
    deletable_spaces.sort(reverse=True)

    print("Solution Part 2", deletable_spaces.pop())
