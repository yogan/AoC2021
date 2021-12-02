def part1(lines):
    distance = 0
    depth = 0

    for line in lines:
        [command, num_str] = line.split(" ")
        number = int(num_str)

        if command == "forward":
            distance += number
        elif command == "up":
            depth -= number
        elif command == "down":
            depth += number

    result = distance * depth
    print("Day 2 part 1:", result)


def part2(lines):
    result = 0
    print("Day 2 part 2:", result)


sample = "day_02/sample.txt"
input_lalisita = "day_02/input-lalisita.txt"
input_yogan = "day_02/input-yogan.txt"

with open(sample) as file:
    lines = file.readlines()
    print("Sample")
    part1(lines)
    part2(lines)

print()

# with open(input_lalisita) as file:
#     lines = file.readlines()
#     print("LaLisita")
#     part1(lines)
#     part2(lines)

# print()

with open(input_yogan) as file:
    lines = file.readlines()
    print("yogan")
    part1(lines)
    part2(lines)
