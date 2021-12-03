input_data = [tuple(int(j) if j.isdigit() else j for j in i.strip("\n")) for i in
              open("./input").readlines()]


def part1():
    print(int(calculate_gamma(input_data), 2) * int(calculate_epsilon(input_data), 2))


def part2():
    print(calculate_oxygen_generator_rating(input_data) * calculate_co2_scrubber_rating(input_data))


def calculate_oxygen_generator_rating(data):
    result = data

    for i in range(len(data[0])):
        if len(result) > 1:
            modal_bit = get_modal_bit_for_position(result, i)
            current_result = result[:]
            for j in result:
                if j[i] != modal_bit:
                    current_result.remove(j)
            result = current_result

    return int(''.join(str(i) for i in result[0]), 2)


def calculate_co2_scrubber_rating(data):
    result = data

    for i in range(len(data[0])):
        if len(result) > 1:
            least_frequent_bit = get_least_frequent_bit_for_position(result, i)
            current_result = result[:]
            for j in result:
                if j[i] != least_frequent_bit:
                    current_result.remove(j)
            result = current_result

    return int(''.join(str(i) for i in result[0]), 2)


def calculate_gamma(data):
    number = ""

    for i in range(0, 12):
        number += str(get_modal_bit_for_position(data, i))

    return number


def calculate_epsilon(data):
    return ''.join('1' if x == '0' else '0' for x in calculate_gamma(data))


def get_modal_bit_for_position(data, position):
    ones = 0
    zeroes = 0

    for i in data:
        if i[position] == 0:
            zeroes += 1
        else:
            ones += 1

    return 1 if ones >= zeroes else 0


def get_least_frequent_bit_for_position(data, position):
    if get_modal_bit_for_position(data, position):
        return 0
    else:
        return 1


part1()
part2()
