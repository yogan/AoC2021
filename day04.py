import re
from input import read_and_solve


def parse_drawn_numbers(line):
    return list(map(int, line.split(",")))


def parse_boards(lines):
    boards = []
    for i in range(len(lines)):
        if lines[i].isspace():
            board = []
            continue
        splits = re.split(r'[ ]+', lines[i].strip())
        board.append(list(map(int, splits)))
        
        if (i+1) % 6 == 0:
            boards.append(board)

    return boards


def part1(lines):
    drawn_numbers = parse_drawn_numbers(lines[0])
    boards = parse_boards(lines[1::])
    return 0


def part2(lines):
    return 0


def test_parse_draw_numbers():
    input = "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1"
    result = parse_drawn_numbers(input)
    assert result == [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24,
                      10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]


def test_parse_boards():
    input = [
        "\n",
        "22 13 17 11  0",
        " 8  2 23  4 24",
        "21  9 14 16  7",
        " 6 10  3 18  5",
        " 1 12 20 15 19",
        "\n",
        " 3 15  0  2 22",
        " 9 18 13 17  5",
        "19  8  7 25 23",
        "20 11 10 24  4",
        "14 21 16 12  6",
        "\n",
        "14 21 17 24  4",
        "10 16 15  9 19",
        "18  8 23 26 20",
        "22 11 13  6  5",
        " 2  0 12  3  7"
    ]

    result = parse_boards(input)
    print(result)
    assert len(result) == 3
    assert len(result[0]) == 5
    assert len(result[0][0]) == 5
    assert result[0][0][0] == 22
    assert result[0][0][4] == 0
    assert result[1][1][1] == 18
    assert result[2][4][4] == 7


test_parse_draw_numbers()
test_parse_boards()
#read_and_solve(__file__, part1, part2)
