from input import read_and_solve


def parse_fish(line):
    return list(map(int, line.split(",")))


def part1(lines):
    days = 80
    fishes = parse_fish(lines[0])

    for _ in range(days):
        new_fishes = []
        spawned_fishes = []
        for fish in fishes:
            if fish == 0:
                new_fishes.append(6)
                spawned_fishes.append(8)
            else:
                new_fishes.append(fish-1)

        new_fishes.extend(spawned_fishes)
        fishes = new_fishes

    return len(fishes)


def part2(lines):
    return 0


read_and_solve(__file__, part1, part2)
