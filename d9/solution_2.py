import json
import os

DISPLAY_VISITS = True
DISPLAY_CURRENT_STATE = False
DISPLAY_MOVEMENTS = True
DISPLAY_RELATIVE_POSITION = False


def parse_file_input(filename):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )

    file_data = []
    with open(os.path.join(__location__, filename), "r") as file_input:
        for line in file_input:
            direction, steps = line.split()
            file_data.append([direction, int(steps)])

    return file_data


def main():
    data = parse_file_input("input.txt")

    states = {
        0: {"x": 0, "y": 0},
        1: {"x": 0, "y": 0},
        2: {"x": 0, "y": 0},
        3: {"x": 0, "y": 0},
        4: {"x": 0, "y": 0},
        5: {"x": 0, "y": 0},
        6: {"x": 0, "y": 0},
        7: {"x": 0, "y": 0},
        8: {"x": 0, "y": 0},
        9: {"x": 0, "y": 0},
    }

    tail_visits = {"0:0"}

    def get_tail_coordinates():
        coordinates = f"{states[9]['x']}:{states[9]['y']}"
        return coordinates

    def are_state_and_state_adjacent(state_1, state_2):
        x_diff = abs(states[state_1]["x"] - states[state_2]["x"])
        y_diff = abs(states[state_1]["y"] - states[state_2]["y"])
        if any([x_diff > 1, y_diff > 1]):
            return False
        return True

    def move_state(_state, _steps, _direction):
        if DISPLAY_MOVEMENTS:
            print("Moving State", _state, "Steps", _steps, "Direction", _direction)

        if _direction == "U":
            states[_state]["y"] += _steps
        if _direction == "D":
            states[_state]["y"] -= _steps
        if _direction == "R":
            states[_state]["x"] += _steps
        if _direction == "L":
            states[_state]["x"] -= _steps

        if _state == 9:
            tail_visits.add(get_tail_coordinates())

    def move_state_diagonally(_state, x, y):
        if DISPLAY_MOVEMENTS:
            print(f"-> Moving State {_state} Diagonally", x, y)

        states[_state]["x"] += x
        states[_state]["y"] += y

        if _state == 9:
            tail_visits.add(get_tail_coordinates())

    def make_state_follow_state(_moving_state, _target_state):
        if are_state_and_state_adjacent(_moving_state, _target_state):
            if DISPLAY_MOVEMENTS:
                print(f"State {_moving_state} is next to State {_target_state}")
                # print(f"-> State {states[_moving_state]} == State {states[_target_state]}")
            return

        if states[_target_state]["y"] == states[_moving_state]["y"]:
            if states[_target_state]["x"] > states[_moving_state]["x"]:
                move_state(_moving_state, 1, "R")
            if states[_target_state]["x"] < states[_moving_state]["x"]:
                move_state(_moving_state, 1, "L")

        if states[_target_state]["x"] == states[_moving_state]["x"]:
            if states[_target_state]["y"] > states[_moving_state]["y"]:
                move_state(_moving_state, 1, "U")
            if states[_target_state]["y"] < states[_moving_state]["y"]:
                move_state(_moving_state, 1, "D")

        # Diagonal cases for head/tail
        if states[_target_state]["x"] > states[_moving_state]["x"]:
            if states[_target_state]["y"] > states[_moving_state]["y"]:
                if DISPLAY_RELATIVE_POSITION:
                    print("Head is RIGHT/TOP of tail")
                move_state_diagonally(_moving_state, 1, 1)

            if states[_target_state]["y"] < states[_moving_state]["y"]:
                if DISPLAY_RELATIVE_POSITION:
                    print("Head is RIGHT/DOWN of tail")
                move_state_diagonally(_moving_state, 1, -1)

        if states[_target_state]["x"] < states[_moving_state]["x"]:
            if states[_target_state]["y"] < states[_moving_state]["y"]:
                if DISPLAY_RELATIVE_POSITION:
                    print("Head is LEFT/DOWN of tail")
                move_state_diagonally(_moving_state, -1, -1)

            if states[_target_state]["y"] > states[_moving_state]["y"]:
                if DISPLAY_RELATIVE_POSITION:
                    print("Head is LEFT/UP of tail")
                move_state_diagonally(_moving_state, -1, 1)

    def all_states_are_adjacent():
        states_connected = []
        for state in states.keys():
            if state == 0:
                continue
            states_connected.append(are_state_and_state_adjacent(state, state - 1))
        return all(states_connected)

    for direction, steps in data:
        print("-->", steps, direction)
        move_state(0, steps, direction)

        while not all_states_are_adjacent():
            print("----> Iteration in Movement", direction, steps)
            for state in states.keys():
                if state == 0:
                    continue
                make_state_follow_state(state, (state - 1))

        print("Finished movements for current iteration")
        print()

    print("Solution Part 2", len(tail_visits))


if __name__ == "__main__":
    main()
