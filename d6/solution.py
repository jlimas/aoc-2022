import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, "input.txt"), "r") as text_input:
    for line in text_input:
        # Part 1: Packet Length 4
        PACKET_LENGTH = 4
        for idx in range(len(line)):
            packet = {*line[0 + idx : PACKET_LENGTH + idx]}
            if len(packet) == PACKET_LENGTH:
                print("Solution Part 1", idx + PACKET_LENGTH)
                break

        # Part 2: Packet Length 14
        PACKET_LENGTH = 14
        for idx in range(len(line)):
            packet = {*line[0 + idx : PACKET_LENGTH + idx]}
            if len(packet) == PACKET_LENGTH:
                print("Solution Part 2", idx + PACKET_LENGTH)
                break
