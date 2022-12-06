import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

strats = {
    # Plays Stone
    "A": {
        "X": 3 + 1,
        "Y": 6 + 2,
        "Z": 0 + 3,
    },
    # Plays Paper
    "B": {
        "X": 0 + 1,
        "Y": 3 + 2,
        "Z": 6 + 3,
    },
    # Plays Scissors
    "C": {
        "X": 6 + 1,
        "Y": 0 + 2,
        "Z": 3 + 3,
    },
}

with open(os.path.join(__location__, "input.txt"), "r") as input:
    # A X Stone = 1
    # B Y Paper = 2
    # C Z Scissors = 3

    score = 0
    for line in input:
        oponent, me = line.split()
        score += strats[oponent][me]

    print("Score Strat #1", score)

with open(os.path.join(__location__, "input.txt"), "r") as input:
    # A X Stone = Loss
    # B Y Paper = Draw
    # C Z Scissors = Win

    score = 0
    for line in input:
        oponent, result = line.split()

        # I have to lose
        if result == "X":
            if oponent == "A":
                score += strats[oponent]["Z"]
            if oponent == "B":
                score += strats[oponent]["X"]
            if oponent == "C":
                score += strats[oponent]["Y"]

        # I have to draw
        if result == "Y":
            if oponent == "A":
                score += strats[oponent]["X"]
            if oponent == "B":
                score += strats[oponent]["Y"]
            if oponent == "C":
                score += strats[oponent]["Z"]

        # I have to win
        if result == "Z":
            if oponent == "A":
                score += strats[oponent]["Y"]
            if oponent == "B":
                score += strats[oponent]["Z"]
            if oponent == "C":
                score += strats[oponent]["X"]

    print("Score Strat #2", score)
