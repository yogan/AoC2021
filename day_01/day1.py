filename = "day_01/input.txt"

with open(filename) as file:
    lines = file.readlines()


def part1(lines):
    prev = int(lines[0])
    increases = 0

    for line in lines[1::]:
        number = int(line)
        if number > prev:
            increases += 1
        prev = number

    print("Day 1 part 1:", increases)


def part2(lines):
    prev = int(lines[0]) + int(lines[1]) + int(lines[2])
    increases = 0

    for i in range(len(lines)-2):
        number = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
        if number > prev:
            increases += 1
        prev = number

    print("Day 1 part 2:", increases)


part1(lines)
part2(lines)
