import unittest
from input import read_and_solve

parens = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

score_for_char = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


def get_first_illegal_char(line):
    stack = []
    for char in line:
        if char in "([{<":
            stack.append(char)
        else:
            expected = stack.pop()
            if char != parens[expected]:
                return char
    return None


def part1(lines):
    illegal_chars = [get_first_illegal_char(line) for line in lines]
    scores = [score_for_char[char] for char in illegal_chars if char]
    return sum(scores)


def part2(lines):
    return 0



class TestDay7(unittest.TestCase):

    sample_lines = [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]",
    ]

    def test_get_first_illegal_char_incomplete(self):
        line = "[({(<(())[]>[[{[]{<()<>>"
        self.assertEqual(get_first_illegal_char(line), None)

    def test_get_first_illegal_char_illegal(self):
        line = "{([(<{}[<>[]}>{[]{[(<()>"
        self.assertEqual(get_first_illegal_char(line), '}')

    def test_part_1_sample(self):
        self.assertEqual(part1(self.sample_lines), 26397
        )

    # def test_part_2_sample(self):
    #     self.assertEqual(part2(self.sample_lines), 168)


if __name__ == '__main__':
    unittest.main(exit=False)
    read_and_solve(__file__, part1, part2)
