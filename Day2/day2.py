input_data = [tuple(int(j) if j.isdigit() else j for j in i.strip("\n").split(" ")) for i in
              open("./input").readlines()]


def part1():
    final_position = follow_instructions_pt1(input_data)
    print(final_position[0] * final_position[1])


def part2():
    final_position = follow_instructions_pt2(input_data)
    print(final_position[0] * final_position[1])


def follow_instructions_pt1(instructions):
    horizontal = 0
    vertical = 0

    for i in instructions:
        if i[0] == "up":
            vertical -= i[1]
        if i[0] == "down":
            vertical += i[1]
        if i[0] == "forward":
            horizontal += i[1]

    return horizontal, vertical


def follow_instructions_pt2(instructions):
    horizontal = 0
    vertical = 0
    aim = 0

    for i in instructions:
        if i[0] == "up":
            aim -= i[1]
        if i[0] == "down":
            aim += i[1]
        if i[0] == "forward":
            horizontal += i[1]
            vertical += aim * i[1]

    return horizontal, vertical


part1()
part2()
