#Advent of Code 2020 - Day8
import copy

def get_input(file):
    with open(file, 'r') as f:
        return f.read().split('\n')

all_conditions = get_input('day8_input.txt')
all_conditions_test = get_input('day8_test.txt')

def day8(input_val):
    accumulator = 0
    unique_vals = []
    counter = 0
    loop = False

    while counter < len(input_val):
        instruction, number = input_val[counter].split(' ')

        if counter not in unique_vals:
            unique_vals.append(counter)
        else:
            loop = True
            break

        if instruction == 'acc':
            accumulator += int(number)
        elif instruction == 'jmp':
            counter += int(number)
            continue
        
        counter += 1
    return accumulator, loop

def day8_pt2(input_val):
    for command in range(len(input_val)):
        instruction, number = input_val[command].split(' ')
        input_val_copy = copy.copy(input_val)

        if instruction == 'nop':
            input_val_copy[command] = 'jmp ' + number
        elif instruction == 'jmp':
            input_val_copy[command] = 'nop ' + number

        current_attempt = day8(input_val_copy)
        if not current_attempt[1]:
            return current_attempt[0]

#print (day8(all_conditions))
print (day8_pt2(all_conditions))