#Advent of Code 2020 - Day 10

def get_input(file):
    with open(file, 'r') as f:
        return [0] + [int(x) for x in f.read().split("\n")]

input_jolts = sorted(get_input("day10_input.txt"))
test_jolts = sorted(get_input("day10_test.txt"))

def use_all(input_val):
    difference_dict = {
        1:0,
        2:0,
        3:1
    }

    for x in range(len(input_val) - 1):
        difference_dict[input_val[x+1] - input_val[x]] += 1

    return difference_dict[1] * difference_dict[3]

print (use_all(input_jolts))


