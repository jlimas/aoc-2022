import copy
import os
import re

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, "input.txt"), "r") as file_input:
    grid = []
    for line in file_input:
        grid.append([int(x) for x in re.findall(r"\d", line)])

    limit = len(grid[0])

    display_initial_grid = False
    display_validating_array = False
    display_validating_array_result = False
    display_debug = False

    if display_initial_grid:
        for i in range(limit):
            print(grid[i])

    def draw_grid(_x, _y):
        _grid = copy.deepcopy(grid)
        _grid[_x][_y] = " "
        for _i in range(len(_grid[0])):
            print([str(c) for c in _grid[_i]])

    def validate_array_decrements(arr, dir):
        if display_validating_array:
            print(f"Visibility {dir}", arr)

        visible_trees = 0
        for i in range(1, len(arr)):
            visible_trees += 1
            if arr[i] >= arr[0]:
                if display_validating_array_result:
                    print("->", False, visible_trees)
                return False, visible_trees

        if display_validating_array_result:
            print("->", True, visible_trees)
        return True, visible_trees

    count = (limit * 4) - 4
    best_scenic_score = 0

    for x in range(0, len(grid[0])):
        for y in range(len(grid[0])):
            current = grid[x][y]

            if x == 0 or y == 0:
                continue

            if x == (limit - 1) or y == (limit - 1):
                continue

            if display_debug:
                print()
                draw_grid(x, y)
                print()

            if display_debug:
                print("Checking to the right")
            right_array = []
            for idx in range(y, limit, 1):
                right_array.append(grid[x][idx])
            right, visible_right = validate_array_decrements(right_array, "right")

            if display_debug:
                print("Checking to the left")
            left_array = []
            for idx in range(y, -1, -1):
                left_array.append(grid[x][idx])
            left, visible_left = validate_array_decrements(left_array, "left")

            if display_debug:
                print("Checking to the top")
            top_array = []
            for idx in range(x, -1, -1):
                top_array.append(grid[idx][y])
            top, visible_top = validate_array_decrements(top_array, "top")

            if display_debug:
                print("Checking to the bottom")
            bottom_array = []
            for idx in range(x, limit, 1):
                bottom_array.append(grid[idx][y])
            bottom, visible_bottom = validate_array_decrements(bottom_array, "bottom")

            if any([left, right, top, bottom]):
                count += 1

            scenic_score = visible_left * visible_right * visible_top * visible_bottom
            if scenic_score >= best_scenic_score:
                best_scenic_score = scenic_score

    print("Solution Part 1", count)
    print("Solution Part 2", best_scenic_score)
