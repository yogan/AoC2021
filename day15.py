from collections import defaultdict
import heapq
import unittest
from input import read_and_solve


def parse_input(lines):
    graph = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            graph[(i, j)] = int(char)
    return graph


def dijkstra(graph):
    x_max, y_max = max(graph.keys())

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    costs = defaultdict(lambda: None)

    queue = []
    heapq.heappush(queue, (0, 0, 0))

    while queue:
        cost, x, y = heapq.heappop(queue)

        if costs[(x, y)] is not None:
            continue

        new_cost = cost + graph[(x, y)]
        costs[(x, y)] = new_cost

        for d in range(len(dx)):
            xx = x + dx[d]
            yy = y + dy[d]
            if xx >= 0 and yy >= 0 and xx <= x_max and yy <= y_max:
                heapq.heappush(queue, (new_cost, xx, yy))

    return costs[(x_max, y_max)] - costs[(0, 0)]


def part1(lines):
    graph = parse_input(lines)
    return dijkstra(graph)


def part2(lines):
    return 0


class TestDay15(unittest.TestCase):

    sample = [
        "1163751742",
        "1381373672",
        "2136511328",
        "3694931569",
        "7463417111",
        "1319128137",
        "1359912421",
        "3125421639",
        "1293138521",
        "2311944581",
    ]

    def test_parse_input(self):
        graph = parse_input(["123", "432"])
        self.assertEqual(graph, {
            (0, 0): 1, (0, 1): 2, (0, 2): 3,
            (1, 0): 4, (1, 1): 3, (1, 2): 2,
        })

    def test_part_1_sample(self):
        self.assertEqual(part1(self.sample), 40)

    # def test_part_2_sample(self):
    #     self.assertEqual(part2(self.sample), TODO)


if __name__ == '__main__':
    unittest.main(exit=False)
    read_and_solve(__file__, part1, part2)
