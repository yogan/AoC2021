import unittest
from input import read_and_solve


def parse_input(lines):
    pos_1 = int(lines[0].split(": ")[1])
    pos_2 = int(lines[1].split(": ")[1])
    return [pos_1, pos_2]


def part1(lines):
    positions = list(map(lambda x: x - 1, parse_input(lines)))
    scores = [0, 0]
    player_index = 0
    rolls = 0
    dice = 0

    while all(map(lambda s: s < 1000, scores)):
        movement = 0
        for _ in range(3):
            dice += 1
            if dice == 101:
                dice = 1
            movement += dice

        rolls += 3

        positions[player_index] = (positions[player_index] + movement) % 10
        scores[player_index] += positions[player_index] + 1

        player_index = (player_index + 1) % len(scores)

    return rolls * min(scores)


def part2(lines):
    positions = list(map(lambda x: x - 1, parse_input(lines)))

    moves = {
        # steps: # of universes
        3: 1,
        4: 3,
        5: 6,
        6: 7,
        7: 6,
        8: 3,
        9: 1,
    }

    players = [
        [(0, positions[0], 1)],
        [(0, positions[1], 1)],
    ]

    counters = [
        [],  # index = throws, value = # of universes
        [],
    ]

    # add more stuff here
    non_winning_universes = [
        [],  # index = throws, value = # of universes
        [],
    ]

    throws = 0

    while any(map(lambda p: p[0] < 21, [*players[0], *players[1]])):
        for index in range(len(players)):
            tuples = []
            # print(players[index])

            non_winning_universes[index].append(0)

            for score, position, universes in players[index]:
                if score >= 21:
                    counters[index].append(universes)
                    continue

                non_winning_universes[index][throws] += universes

                new_positions = {}  # {new_pos: #_univ}

                for steps, next_universes in moves.items():
                    new_position = (position + steps) % 10
                    new_positions[new_position] = universes * next_universes

                new_tuples = [(score + pos + 1, pos, univ)
                              for pos, univ in new_positions.items()]
                tuples.extend(new_tuples)

            players[index] = tuples

        throws += 1

    foo1 = [c * n for c, n in zip(counters[0], non_winning_universes[1])]
    foo2 = [c * n for c, n in zip(counters[1], non_winning_universes[0])]

    sum1 = sum(foo1)
    sum2 = sum(foo2)

    return max(sum1, sum2)


class TestDay21(unittest.TestCase):

    sample = [
        "Player 1 starting position: 4",
        "Player 2 starting position: 8",
    ]

    def test_parse_input(self):
        [pos_1, pos_2] = parse_input(self.sample)
        self.assertEqual(pos_1, 4)
        self.assertEqual(pos_2, 8)

    def test_part_1_sample(self):
        self.assertEqual(part1(self.sample), 739785)

    def test_part_2_sample(self):
        self.assertEqual(part2(self.sample), 444356092776315)


if __name__ == '__main__':
    unittest.main(exit=False)
    read_and_solve(__file__, part1, part2)
