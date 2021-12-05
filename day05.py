import unittest
from typing import Dict
from input import read_and_solve


def line_to_coords(line):
    return tuple(
        map(lambda cs: tuple(map(int, cs.split(","))),
            line.split(" -> ")))


def covered_points(start, end):
    x1, y1 = start
    x2, y2 = end
    points = set()

    if x1 == x2:
        y_min = min(y1, y2)
        y_max = max(y1, y2)
        for y in range(y_min, y_max + 1):
            points.add((x1, y))
        return points

    elif y1 == y2:
        x_min = min(x1, x2)
        x_max = max(x1, x2)
        for x in range(x_min, x_max + 1):
            points.add((x, y1))
        return points

    else:
        # for now, we only consider horizontal or vertical lines
        return points


def count_points(points_with_count: Dict, points):
    for point in points:
        if point in points_with_count:
            points_with_count[point] += 1
        else:
            points_with_count[point] = 1


def filter_points_with_min_count(points_with_count: Dict, min):
    return {k: v for k, v in points_with_count.items() if v >= min}


def part1(lines):
    points_with_count = {}

    for line in lines:
        start, end = line_to_coords(line)
        points = covered_points(start, end)
        count_points(points_with_count, points)

    dangerous_points = filter_points_with_min_count(points_with_count, 2)
    return len(dangerous_points)


def part2(lines):
    return 0


class TestDay5(unittest.TestCase):

    def test_line_to_coords(self):
        result = line_to_coords('741,11 -> 466,11')
        self.assertEqual(result, ((741, 11), (466, 11)))

    def test_covered_points_horizontal(self):
        result = covered_points((1, 1), (1, 3))
        self.assertEqual(result, {(1, 1), (1, 2), (1, 3)})

    def test_covered_points_horizontal_backwards(self):
        result = covered_points((1, 3), (1, 1))
        self.assertEqual(result, {(1, 1), (1, 2), (1, 3)})

    def test_covered_points_vertical(self):
        result = covered_points((1, 1), (3, 1))
        self.assertEqual(result, {(1, 1), (2, 1), (3, 1)})

    def test_covered_points_vertical_backwards(self):
        result = covered_points((3, 1), (1, 1))
        self.assertEqual(result, {(1, 1), (2, 1), (3, 1)})

    def test_count_points(self):
        points = {}
        count_points(points, {(3, 1), (1, 1), (2, 1)})
        self.assertEqual(points, {(1, 1): 1, (2, 1): 1, (3, 1): 1})
        count_points(points, {(3, 1), (1, 1)})
        self.assertEqual(points, {(1, 1): 2, (2, 1): 1, (3, 1): 2})
        count_points(points, {(9, 9), (1, 1)})
        self.assertEqual(points, {(1, 1): 3, (2, 1): 1, (3, 1): 2, (9, 9): 1})

    def test_filter_points_with_min_count(self):
        points = filter_points_with_min_count(
            {(1, 1): 3, (2, 1): 1, (3, 1): 2, (9, 9): 1},
            2)
        self.assertEqual(points, {(1, 1): 3, (3, 1): 2})

    def test_part_1(self):
        lines = [
            "0,9 -> 5,9",
            "8,0 -> 0,8",
            "9,4 -> 3,4",
            "2,2 -> 2,1",
            "7,0 -> 7,4",
            "6,4 -> 2,0",
            "0,9 -> 2,9",
            "3,4 -> 1,4",
            "0,0 -> 8,8",
            "5,5 -> 8,2",
        ]
        self.assertEqual(part1(lines), 5)


if __name__ == '__main__':
    unittest.main(exit=False)
    print()
    read_and_solve(__file__, part1, part2)
