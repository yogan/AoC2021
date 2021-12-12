import unittest
from input import read_and_solve
from collections import defaultdict, deque

def parse_edges(lines):
    graph = defaultdict(set)

    for line in lines:
        start, end = line.split("-")
        if end != "end":
            graph[start].add(end)
            graph[end].add(start)

    return graph

discovered = set()

def dfs(graph, v, stack, paths):
    cur_path = paths[-1]

    discovered.add(v)
    stack.append(v)
    cur_path.append(v)

    if v == "end":
        paths.append([])
    else:
        for w in graph[v]:
            if not w in discovered:
                dfs(graph, w, stack, paths)

    stack.pop()
    discovered.remove(v)

def find_paths(graph):
    paths = [[]]
    dfs(graph, "start", [], paths)
    print(paths)
    return len(paths)


def part1(lines):
    graph = parse_edges(lines)
    paths = find_paths(graph)
    return len(paths)


def part2(lines):
    return 0


class TestDay12(unittest.TestCase):

    sample_1 = [
        "start-A",
        "start-b",
        "A-c",
        "A-b",
        "b-d",
        "A-end",
        "b-end",
    ]

    def test_parse_edges(self):
        graph = parse_edges(self.sample_1)
        self.assertEqual(graph, {
            "start": {"A", "b"},
            "A":     {"c", "b", "end", "start"},
            "b":     {"start", "A", "d", "end"},
            "c":     {"A"},
            "d":     {"b"},
        })

    def test_parse_edges(self):
        graph = {
            "start": {"A", "b"},
            "A":     {"c", "b", "end", "start"},
            "b":     {"start", "A", "d", "end"},
            "c":     {"A"},
            "d":     {"b"},
        }
        find_paths(graph)

    # def test_part_1_sample_1(self):
    #     self.assertEqual(part1(self.sample_1), 10)

    # def test_part_2_sample_1(self):
    #     self.assertEqual(part2(self.sample_1), 288957)


if __name__ == '__main__':
    unittest.main(exit=False)
    read_and_solve(__file__, part1, part2)
