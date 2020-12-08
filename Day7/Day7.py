#Advent of Code 2020 - Day7
import re

def get_input(file):
    with open(file, 'r') as f:
        return f.read().split('\n')

all_conditions = get_input('day7_input.txt')
all_conditions_test = get_input('day7_test.txt')

def add_all_bags(input_val):
    all_bags = {}
    for condition in input_val:
        regex_pattern = r'(\d?\s?\w+\s\w+)\sbags?'
        condition_split = re.findall(regex_pattern, condition)
        key, vals = condition_split[0], condition_split[1:]
        all_bags[key] = []
        for val in vals:
            if val != ' no other':
                all_bags[key].append({val[2:]:val[0]})
    return all_bags

all_bags = add_all_bags(all_conditions_test)
#all_bags = add_all_bags(all_conditions)
#print (all_bags)

unique_bags = set()
def find_unique_upwards(bag_sought):
    for other_bag in all_bags.keys():
        for element in all_bags[other_bag]:
            if bag_sought in element.keys():
                unique_bags.add(other_bag)
                find_unique_upwards(other_bag)
#----------------------------------------------------
# counter = 0
# def find_unique_downwards(bag_sought):
#     for bag_contained in all_bags[bag_sought]:
#         for bag in bag_contained.keys():
#             global counter
#             counter += int(bag_contained[bag])
#             for x in range(int(bag_contained[bag])):
#                 find_unique_downwards(bag)
#----------------------------------------------------

#find_unique_upwards('shiny gold')
#print (len(unique_bags))

#find_unique_downwards('shiny gold')
#print (counter)

def find_unique_downwards_2(bag_sought):
    counter_recursive = 0
    if all_bags[bag_sought] == []:
        return 0
    for bag_contained in all_bags[bag_sought]:
    #####for new_bag in [list(x.keys())[0] for x in all_bags[bag_sought]]:
        #####print (new_bag)
        new_bag = list(bag_contained.keys())[0]
        counter_recursive += int(bag_contained[new_bag]) * (1 + find_unique_downwards_2(new_bag))
        #####counter_recursive += int(all_bags[bag_sought][all_bags[bag_sought].index(new_bag)]) * (1 + find_unique_downwards_2(new_bag)) 
    return counter_recursive

print (find_unique_downwards_2('shiny gold'))