import copy
import os
import re


def find(string, ch):
    return [int(i / 4) + 1 for i, ltr in enumerate(string) if ltr == ch]


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, "input.txt"), "r") as input:
    stack = {}
    stacks = []

    # Create the stacks
    for line in input:
        if "1" not in line:
            continue

        if "move" in line:
            continue

        stacks = [int(x) for x in [*line.split()]]

    for s in stacks:
        stack[s] = []

    # Fill the stacks
    input.seek(0)
    for line in input:
        if "1" in line:
            continue

        if "move" in line:
            continue

        if "[" in line:
            # Get the stack column position
            positions = find(line, "[")
            # Get the stack column value
            values = re.findall(r"\[(.)]", line)

            # Fill the stack with values
            for idx in range(len(positions)):
                stack[positions[idx]].append(values[idx])

    # Fix the order of the stack items
    for key in stack.keys():
        stack[key] = list(reversed(stack[key]))

    # Create a copy of the stack
    stack_2 = copy.deepcopy(stack)

    # Start following the move actions of part 1
    input.seek(0)
    for line in input:
        if "move" not in line:
            continue

        # Parse the movement actions
        moves, move_from, move_to = [int(x) for x in re.findall(r"\d+", line)]

        # Perform the stack movement
        for move in range(moves):
            value = stack[move_from].pop()
            stack[move_to].append(value)

    top_crates = []
    for key in stack.keys():
        top_crates.append(stack[key].pop())

    print("Solution Part 1", "".join(top_crates))

    # Start following the move actions of part 2
    # This time we are moving all the crates in one move
    input.seek(0)
    for line in input:
        if "move" not in line:
            continue

        # Parse the movement actions
        moves, move_from, move_to = [int(x) for x in re.findall(r"\d+", line)]

        # Perform the stack movement
        values = stack_2[move_from][-moves:]
        del stack_2[move_from][-moves:]
        stack_2[move_to] = [*stack_2[move_to], *values]

    top_crates = []
    for key in stack_2.keys():
        top_crates.append(stack_2[key].pop())

    print("Solution Part 2", "".join(top_crates))
