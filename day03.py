from input import read_and_solve


def part1(lines):
    digits = len(lines[0])-1
    most_common_bits = [0] * digits

    for line in lines:
        line_bits = list(line)
        for i in range(digits):
            bit = line_bits[i]
            if bit == '0':
                most_common_bits[i] -= 1
            else:
                most_common_bits[i] += 1

    gamma_bits = [0] * digits
    epsilon_bits = [0] * digits
    for i in range(digits):
        if most_common_bits[i] > 0:
            gamma_bits[i] = "1"
            epsilon_bits[i] = "0"
        else:
            gamma_bits[i] = "0"
            epsilon_bits[i] = "1"

    gamma = int("".join(gamma_bits), 2)
    epsilon = int("".join(epsilon_bits), 2)

    return gamma * epsilon


def part2(lines):
    return 0


read_and_solve(__file__, part1, part2)
