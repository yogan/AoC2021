import unittest
from input import read_and_solve
from collections import defaultdict, deque


def parse_edges(lines):
    graph = defaultdict(set)

    for line in lines:
        start, end = line.split("-")
        graph[start].add(end)
        graph[end].add(start)

    return graph


def dfs(graph, v, visited, cur_path, paths):
    cur_path.append(v)

    if not v.isupper():
        visited.add(v)

    if v == "end":
        paths.append([*cur_path])
    else:
        for w in graph[v]:
            if not w in visited:
                dfs(graph, w, visited, cur_path, paths)

    cur_path.pop()

    if not v.isupper():
        visited.remove(v)


def find_paths(graph):
    paths = []
    visited = set()
    dfs(graph, "start", visited, [], paths)
    return paths


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

    sample_2 = [
        "dc-end",
        "HN-start",
        "start-kj",
        "dc-start",
        "dc-HN",
        "LN-dc",
        "HN-end",
        "kj-sa",
        "kj-HN",
        "kj-dc",
    ]

    sample_3 = [
        "fs-end",
        "he-DX",
        "fs-he",
        "start-DX",
        "pj-DX",
        "end-zg",
        "zg-sl",
        "zg-pj",
        "pj-he",
        "RW-he",
        "fs-DX",
        "pj-RW",
        "zg-RW",
        "start-pj",
        "he-WI",
        "zg-he",
        "pj-fs",
        "start-RW",
    ]

    def test_parse_edges(self):
        graph = parse_edges(self.sample_1)
        self.assertEqual(graph, {
            "start": {"A", "b"},
            "A":     {"c", "b", "end", "start"},
            "b":     {"start", "A", "d", "end"},
            "c":     {"A"},
            "d":     {"b"},
            "end":   {"A", "b"}
        })

    def test_find_paths(self):
        graph = {
            "start": {"A", "b"},
            "A":     {"c", "b", "end", "start"},
            "b":     {"start", "A", "d", "end"},
            "c":     {"A"},
            "d":     {"b"},
            "end":   {"A", "b"}
        }
        expected_path_strings = {
            "start,A,b,A,c,A,end",
            "start,A,b,A,end",
            "start,A,b,end",
            "start,A,c,A,b,A,end",
            "start,A,c,A,b,end",
            "start,A,c,A,end",
            "start,A,end",
            "start,b,A,c,A,end",
            "start,b,A,end",
            "start,b,end",
        }
        paths = find_paths(graph)
        path_strings = {",".join(path) for path in paths}
        self.assertEqual(path_strings, expected_path_strings)

    def test_part_1_sample_1(self):
        self.assertEqual(part1(self.sample_1), 10)

    def test_part_1_sample_2(self):
        self.assertEqual(part1(self.sample_2), 19)

    def test_part_1_sample_3(self):
        self.assertEqual(part1(self.sample_3), 226)

    # def test_part_2_sample_1(self):
    #     self.assertEqual(part2(self.sample_1), 288957)


if __name__ == '__main__':
    unittest.main(exit=False)
    read_and_solve(__file__, part1, part2)
