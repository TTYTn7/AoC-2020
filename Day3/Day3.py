#Advent of Code 2020 - Day 3
import sys
sys.path.append('/home/trackback/Desktop/AoC-2020')
from Utilities import read_list

input_list = read_list(3)
input_list_test = read_list(3, 'test')

def day3(input_val):

	slopes = ([1,1], [3,1], [5,1], [7,1], [1,2])
	nums = []

	for slope in slopes:
		row_increase, col_increase = slope
		row, col, num_trees = 0, 0, 0

		while col < len(input_val):
			check = input_val[col][row]
			if check == '#':
				num_trees += 1
			row = (row + row_increase) % len(input_val[0])
			col += col_increase
		
		nums.append(num_trees)

	ans = nums[0]
	for x in nums[1:]:
		ans *= x

	return 'done', ans

#print (day3(input_list_test))
print (day3(input_list))