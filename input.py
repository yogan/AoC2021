def read_and_solve(filename, solve_part_1, solve_part_2):
    day = filename.replace("day", "").replace(".py", "")

    input_sample   = f"inputs/{day}/sample.txt"
    input_lalisita = f"inputs/{day}/lalisita.txt"
    input_yogan    = f"inputs/{day}/yogan.txt"

    def process(input, name):
        with open(input) as file:
            lines = file.readlines()
            print(name)
            print('-' * len(name))
            print("Part 1:", solve_part_1(lines))
            print("Part 2:", solve_part_2(lines))

    print("========")
    print(f" DAY {day}")
    print("========")
    print()

    process(input_sample,   "Sample")
    print()
    process(input_lalisita, "LaLisita")
    print()
    process(input_yogan,    "yogan")

