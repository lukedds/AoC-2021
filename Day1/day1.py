input_data = [int(i) for i in open("./input").readlines()]


def part_one(data):
    return sum(1 for i, v in enumerate(data) if v > data[i-1])

def part_two(data):
    return part_one([data[i] + data[i-1] + data[i-2] for i in range(2, len(data))])


print(part_one(input_data))
print(part_two(input_data))
