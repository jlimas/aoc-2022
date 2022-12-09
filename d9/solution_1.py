import os

DISPLAY_DIFFS = False
DISPLAY_VISITS = False
DISPLAY_CURRENT_STATE = False
DISPLAY_MOVEMENTS = False
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

    head_state = {"x": 0, "y": 0}
    tail_state = {"x": 0, "y": 0}
    tail_visits = {"0:0"}

    def get_tail_coordinates():
        coordinates = f"{tail_state['x']}:{tail_state['y']}"
        if DISPLAY_VISITS:
            print("Tail Visiting", coordinates)
        return coordinates

    def get_current_state():
        if not DISPLAY_CURRENT_STATE:
            return

        print()
        print(f"--> Head Currently (X:{head_state['x']}) (Y:{head_state['y']})")
        print(f"--> Tail Currently (X:{tail_state['x']}) (Y:{tail_state['y']})")
        print("--> Tail has visited", len(tail_visits))

    def are_head_and_tail_adjacent():
        x_diff = abs(head_state["x"] - tail_state["x"])
        if DISPLAY_DIFFS:
            print("X Diff", x_diff)

        y_diff = abs(head_state["y"] - tail_state["y"])
        if DISPLAY_DIFFS:
            print("Y Diff", y_diff)

        if any([x_diff > 1, y_diff > 1]):
            return False

        return True

    def move_head(_steps, _direction):
        if DISPLAY_MOVEMENTS:
            print("Moving Head", _steps, "Direction", _direction)
            print()

        if _direction == "U":
            head_state["y"] += _steps
        if _direction == "D":
            head_state["y"] -= _steps
        if _direction == "R":
            head_state["x"] += _steps
        if _direction == "L":
            head_state["x"] -= _steps

    def move_tail(_steps, _direction):
        if DISPLAY_MOVEMENTS:
            print("-> Moving Tail", _steps, "Direction", _direction)

        if _direction == "U":
            tail_state["y"] += _steps
        if _direction == "D":
            tail_state["y"] -= _steps
        if _direction == "R":
            tail_state["x"] += _steps
        if _direction == "L":
            tail_state["x"] -= _steps

        tail_visits.add(get_tail_coordinates())

    def move_tail_diagonally(x, y):
        if DISPLAY_MOVEMENTS:
            print("-> Moving Tail Diagonally", x, y)

        tail_state["x"] += x
        tail_state["y"] += y
        tail_visits.add(get_tail_coordinates())

    def make_tail_follow_head():
        if are_head_and_tail_adjacent():
            if DISPLAY_MOVEMENTS:
                print("Tail is next to the head, no movement needed")
            return

        if head_state["y"] == tail_state["y"]:
            if head_state["x"] > tail_state["x"]:
                while not are_head_and_tail_adjacent():
                    move_tail(1, "R")

            if head_state["x"] < tail_state["x"]:
                while not are_head_and_tail_adjacent():
                    move_tail(1, "L")

        if head_state["x"] == tail_state["x"]:
            if head_state["y"] > tail_state["y"]:
                while not are_head_and_tail_adjacent():
                    move_tail(1, "U")
            if head_state["y"] < tail_state["y"]:
                while not are_head_and_tail_adjacent():
                    move_tail(1, "D")

        # Diagonal cases for head/tail
        if head_state["x"] > tail_state["x"]:
            if head_state["y"] > tail_state["y"]:
                if DISPLAY_RELATIVE_POSITION:
                    print("Head is RIGHT/TOP of tail")
                move_tail_diagonally(1, 1)
                make_tail_follow_head()

            if head_state["y"] < tail_state["y"]:
                if DISPLAY_RELATIVE_POSITION:
                    print("Head is RIGHT/DOWN of tail")
                move_tail_diagonally(1, -1)
                make_tail_follow_head()

        if head_state["x"] < tail_state["x"]:
            if head_state["y"] < tail_state["y"]:
                if DISPLAY_RELATIVE_POSITION:
                    print("Head is LEFT/DOWN of tail")
                move_tail_diagonally(-1, -1)
                make_tail_follow_head()

            if head_state["y"] > tail_state["y"]:
                if DISPLAY_RELATIVE_POSITION:
                    print("Head is LEFT/UP of tail")
                move_tail_diagonally(-1, 1)
                make_tail_follow_head()

    for direction, steps in data:
        move_head(steps, direction)
        make_tail_follow_head()
        get_current_state()

    print("Solution Part 1", len(tail_visits))


if __name__ == "__main__":
    main()
