#Advent of Code Day 6 - 2020
with open('day6_input.txt', 'r') as f:
    all_groups = f.read().split('\n\n')

def day6(input_val):
    # Part 1
    ans_first, ans_second = 0, 0
    for group in input_val:
        answers = [x for x in group.replace('\n', '')]
        ans_first += len(set(answers))
    # Part 2
    for group in input_val:
        initial = list(group.split('\n')[0])
        for answer in group.split('\n')[1:]:
            initial = [x for x in initial if x in answer]
        ans_second += len(initial)
    
    return ans_first, ans_second

print ('done', day6(all_groups))