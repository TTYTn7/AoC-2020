#Advent of Code 2020 - Day 1
import sys
sys.path.append('/home/trackback/Desktop/AoC-2020')
from Utilities import read_list

input_list = read_list(1)
input_list_test = read_list(1, 'test')

def find2020(input):
	for n1 in range(len(input_list)):
		for n2 in range(n1, len(input_list)):
			for n3 in range(n2, len(input_list)):
				if input_list[n1] + input_list[n2] + input_list[n3] == 2020:
					return input_list[n1]*input_list[n2]*input_list[n3]

print (find2020(input_list))
