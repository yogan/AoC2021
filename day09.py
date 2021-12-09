from input import read_and_solve


def parse_input(lines):
    result = []
    for line in lines:
        heights = [int(digit) for digit in line]
        result.append(heights)
    return result


def get_neighbors(height_map, row, column, row_max, column_max):
    result = []
    if row > 0:
        result.append(height_map[row-1][column])
    if row < row_max:
        result.append(height_map[row+1][column])
    if column > 0:
        result.append(height_map[row][column-1])
    if column < column_max:
        result.append(height_map[row][column+1])
    return result


def part1(lines):
    height_map = parse_input(lines)
    sum_of_risk_levels = 0
    row_max = len(height_map)
    column_max = len(height_map[0])
    for row in range(row_max):
        for column in range(column_max):
            risk_level = height_map[row][column]
            neighbors = get_neighbors(
                height_map, row, column, row_max-1, column_max-1)
            larger_neighbors = [x for x in neighbors if x > risk_level]
            if len(neighbors) == len(larger_neighbors):
                sum_of_risk_levels += risk_level + 1

    return sum_of_risk_levels


def part2(lines):
    return 0


read_and_solve(__file__, part1, part2)
