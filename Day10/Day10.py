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

#print (use_all(input_jolts))

def find_all_combinations(input_val):
    full_tree = {0:[]}

    for x in range(len(input_val)):
        current_element = input_val[x]

        try:
            first_next_element = input_val[x+1]
        except IndexError:
            first_next_element = 9999999999999
        
        try:
            second_next_element = input_val[x+2]
        except IndexError:
            second_next_element = 9999999999999

        try:
            third_next_element = input_val[x+3]
        except IndexError:
            third_next_element = 99999999999999

        #next_three = [input_val[x+1], input_val[x+2], input_val[x+3]]

        if first_next_element - current_element in [1,2,3]:
            full_tree[current_element].append(first_next_element)
            full_tree[first_next_element] = []
        
        if second_next_element - current_element in [2,3]:
            full_tree[current_element].append(second_next_element)
            full_tree[second_next_element] = []

        if third_next_element - current_element == 3:
            full_tree[current_element].append(third_next_element)
            full_tree[third_next_element] = []
           
    return full_tree

print (find_all_combinations(test_jolts))

def part2(input_val):
    tree = find_all_combinations(input_val)
    input_val = input_val[::-1]
    paths = {}
    last_split = 1

    for x in range(len(input_val)):
        current_adapter = input_val[x]
        if len(tree[current_adapter]) > 1:
            paths[current_adapter] = sum(paths[x] for x in tree[current_adapter])
            last_split = paths[current_adapter]
        else:
            paths[current_adapter] = last_split
    
    return paths[0]

print (part2(input_jolts))