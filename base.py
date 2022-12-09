import os


def parse_file_input(filename):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )

    file_data = []
    with open(os.path.join(__location__, filename), "r") as file_input:
        for line in file_input:
            file_data.append(line)

    return file_data


if __name__ == "__main__":
    data = parse_file_input("input.txt")
    print(data)
