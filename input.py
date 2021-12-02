def read_and_solve(filename, solve_part_1, solve_part_2):
    day = filename.replace("day", "").replace(".py", "")

    input_sample   = f"inputs/{day}/sample.txt"
    input_lalisita = f"inputs/{day}/lalisita.txt"
    input_yogan    = f"inputs/{day}/yogan.txt"

    print("========")
    print(f" DAY {day}")
    print("========")
    print()

    with open(input_sample) as file:
        lines = file.readlines()
        print("Sample")
        print("------")
        print("Part 1:", solve_part_1(lines))
        print("Part 2:", solve_part_2(lines))

    print()

    with open(input_lalisita) as file:
        lines = file.readlines()
        print("LaLisita")
        print("--------")
        print("Part 1:", solve_part_1(lines))
        print("Part 2:", solve_part_2(lines))

    print()

    with open(input_yogan) as file:
        lines = file.readlines()
        print("yogan")
        print("-----")
        print("Part 1:", solve_part_1(lines))
        print("Part 2:", solve_part_2(lines))
