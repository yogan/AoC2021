import unittest
from input import read_and_solve


def parse_positions(line):
    return list(map(int, line.split(",")))


def map_to_fuel(positions, target):
    return list(map(lambda x: abs(x - target), positions))


def calculate_fuel_histogram(positions):
    pos_min = min(positions)
    pos_max = max(positions)

    histogram = {}
    for p in range(pos_min, pos_max + 1):
        histogram[p] = sum(map_to_fuel(positions, p))

    return histogram


def part1(lines):
    positions = parse_positions(lines[0])
    fuel_histogram = calculate_fuel_histogram(positions)
    return min(fuel_histogram.values())


def part2(lines):
    return 0


class TestDay7(unittest.TestCase):

    sample_lines = ["16,1,2,0,4,2,7,1,2,14"]

    def test_parse_positions(self):
        positions = parse_positions(self.sample_lines[0])
        self.assertEqual(positions, [16, 1, 2, 0, 4, 2, 7, 1, 2, 14])

    def test_map_to_fuel(self):
        fuels = map_to_fuel([0, 1, 2, 3, 7, 1, 0], 2)
        self.assertEqual(fuels, [2, 1, 0, 1, 5, 1, 2])

    def test_calculate_fuel_histogram(self):
        histogram = calculate_fuel_histogram([2, 1, 1, 4, 2])
        self.assertEqual(histogram, {
            1: 1 + 0 + 0 + 3 + 1,
            2: 0 + 1 + 1 + 2 + 0,
            3: 1 + 2 + 2 + 1 + 1,
            4: 2 + 3 + 3 + 0 + 2,
        })

    def test_calculate_fuel_histogram_sample(self):
        histogram = calculate_fuel_histogram([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])
        self.assertEqual(histogram[2], 37)
        self.assertEqual(histogram[1], 41)
        self.assertEqual(histogram[3], 39)
        self.assertEqual(histogram[10], 71)

    def test_part_1_sample(self):
        self.assertEqual(part1(self.sample_lines), 37)

    # def test_part_2_sample(self):
    #     self.assertEqual(part2(self.sample_lines), "TODO")


if __name__ == '__main__':
    unittest.main(exit=False)
    print()
    read_and_solve(__file__, part1, part2)
