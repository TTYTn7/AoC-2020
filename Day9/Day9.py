#Advent of Code 2020 - Day 9

def get_input(file):
    with open(file, 'r') as f:
        return [int(x) for x in f.read().split('\n')]

all_numbers = get_input('day9_input.txt')
all_numbers_test = get_input('day9_test.txt')

def day9(input_val, preamble=25):
    for next_number in range(preamble, len(input_val)):
        considered_set = input_val[next_number-preamble:next_number]
        found = False
        for previous_number in considered_set:
            considered_set_copy = considered_set[:]
            considered_set_copy.remove(previous_number)
            if input_val[next_number] - previous_number in considered_set_copy:
                found = True
        if not found:
            wrong_number = input_val[next_number]
            break
            # Part 1:
            # return wrong_number
    
    ans = day9_pt2(input_val[:next_number], wrong_number)
    return min(ans) + max(ans)


def day9_pt2(input_val, wrong_number):
    # Recursive ----------------------------------------------------------
    # nums_checked = []
    # for first_num in range(len(input_val)):
    #     current_total = input_val[first_num] + sum(nums_checked)
    #     nums_checked.append(input_val[first_num])
    #     if current_total == wrong_number:
    #         return nums_checked
    #     elif current_total > wrong_number:
    #         return day9_pt2(input_val[1:], wrong_number)
    # Recursive ----------------------------------------------------------
    
    for first_num in range(len(input_val)):
        nums_checked = [input_val[first_num]]
        current_total = input_val[first_num]
        for next_num in range(first_num+1, len(input_val)):
            nums_checked.append(input_val[next_num])
            current_total += input_val[next_num]
            if current_total == wrong_number:
                print ('Hit')
                return nums_checked
            elif current_total > wrong_number:
                break

#print (day9(all_numbers_test, 5))
print (day9(all_numbers))