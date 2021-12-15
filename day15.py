from collections import defaultdict, deque
from math import inf
import unittest
from input import read_and_solve


def parse_input(lines):
    graph = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            graph[(i, j)] = int(char)
    return graph


def find_neighbors(u, Q):
    # assert u not in Q
    ui, uj = u
    return {(i, j) for i, j in Q if
            (abs(ui - i) == 1 and uj == j) or
            (abs(uj - j) == 1 and ui == i)}


def dijkstra(graph):
    start = (0, 0)
    end = max(graph.keys())

    dist = defaultdict(lambda: inf)
    prev = dict()
    Q = set(graph.keys())

    dist[start] = 0

    while Q:
        distances = {(i, j): dist[(i, j)] for i, j in Q}
        u = min(distances, key=distances.get)

        Q.remove(u)

        if u == end:
            break

        for v in find_neighbors(u, Q):
            alt = dist[u] + graph[v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    # S = deque()
    total_risk = 0
    u = end

    while True:
        # S.appendleft(u)
        if u != start:
            total_risk += graph[u]
        if u not in prev:
            break
        u = prev[u]

    return total_risk


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

    def test_find_neighbors(self):
        Q = {
                    (0, 1),
            (1, 0), (1, 1),
            (2, 0),         (2, 2), (2, 3),
            (3, 0), (3, 1), (3, 2), (3, 3),
            (4, 0), (4, 1),
                    (5, 1),         (5, 3),
        }
        self.assertEqual(find_neighbors((0, 0), Q), {
                    (0, 1),
            (1, 0),
        })
        self.assertEqual(find_neighbors((2, 1), Q), {
                    (1, 1),
            (2, 0),         (2, 2),
                    (3, 1),
        })
        self.assertEqual(find_neighbors((4, 2), Q), {
                    (3, 2),
            (4, 1),
        })
        self.assertEqual(find_neighbors((5, 0), Q), {
            (4, 0),
                    (5, 1),
        })
        self.assertEqual(find_neighbors((5, 4), Q), {(5, 3)})

    def test_part_1_sample(self):
        self.assertEqual(part1(self.sample), 40)

    # def test_part_2_sample(self):
    #     self.assertEqual(part2(self.sample), TODO)


if __name__ == '__main__':
    unittest.main(exit=False)
    read_and_solve(__file__, part1, part2)
