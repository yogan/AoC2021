from typing import Counter
import unittest
from input import read_and_solve


def parse_input(lines):
    template_line, rule_lines = (lines[0], lines[2:])

    template = list(template_line)

    rule_pairs = [list(rule.split(" -> ")) for rule in rule_lines]
    rules = {key: value for key, value in rule_pairs}

    return template, rules


def step(template, rules):
    new_template = []

    for i in range(len(template) - 1):
        c1, c2 = template[i], template[i+1]
        to_insert = rules[c1 + c2]
        new_template.append(c1)
        new_template.append(to_insert)

    new_template.append(template[-1])

    return new_template


def find_extremes(template):
    histogram = Counter(template)
    counts = histogram.values()
    return min(counts), max(counts)


def part1(lines):
    template, rules = parse_input(lines)

    for _ in range(10):
        template = step(template, rules)

    min, max = find_extremes(template)
    return max - min


def part2(lines):
    template, rules = parse_input(lines)

    for _ in range(40):
        template = step(template, rules)

    min, max = find_extremes(template)
    return max - min



class TestDay14(unittest.TestCase):

    sample = [
        "NNCB",
        "",
        "CH -> B",
        "HH -> N",
        "CB -> H",
        "NH -> C",
        "HB -> C",
        "HC -> B",
        "HN -> C",
        "NN -> C",
        "BH -> H",
        "NC -> B",
        "NB -> B",
        "BN -> B",
        "BB -> N",
        "BC -> B",
        "CC -> N",
        "CN -> C",
    ]

    def test_parse_input(self):
        template, rules = parse_input(self.sample)
        self.assertEqual(template, ['N', 'N', 'C', 'B'])
        self.assertEqual(rules, {
            "CH": "B",
            "HH": "N",
            "CB": "H",
            "NH": "C",
            "HB": "C",
            "HC": "B",
            "HN": "C",
            "NN": "C",
            "BH": "H",
            "NC": "B",
            "NB": "B",
            "BN": "B",
            "BB": "N",
            "BC": "B",
            "CC": "N",
            "CN": "C",
        })

    def test_step(self):
        result = step(list("NNCB"), {
            "CH": "B",
            "HH": "N",
            "CB": "H",
            "NH": "C",
            "HB": "C",
            "HC": "B",
            "HN": "C",
            "NN": "C",
            "BH": "H",
            "NC": "B",
            "NB": "B",
            "BN": "B",
            "BB": "N",
            "BC": "B",
            "CC": "N",
            "CN": "C",
        })
        self.assertEqual(result, list("NCNBCHB"))

    def test_find_extremes(self):
        min, max = find_extremes("AAACAAABBDDDAAA")
        self.assertEqual(min, 1)
        self.assertEqual(max, 3 * 3)

    def test_part_1_sample(self):
        self.assertEqual(part1(self.sample), 1588)

    # def test_part_2_sample(self):
    #     self.assertEqual(part2(self.sample), TODO)


if __name__ == '__main__':
    unittest.main(exit=False)
    read_and_solve(__file__, part1, part2)
