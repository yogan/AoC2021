from input import read_and_solve


def calc_most_common_bit(numbers, index):
    most_common_bit = 0

    for number in numbers:
        line_bits = list(number)
        bit = line_bits[index]
        if bit == '0':
            most_common_bit -= 1
        else:
            most_common_bit += 1

    return most_common_bit

def part1(lines):
    digits = len(lines[0]) - 1

    gamma_bits = [0] * digits
    epsilon_bits = [0] * digits

    for i in range(digits):
        if calc_most_common_bit(lines, i) > 0:
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
