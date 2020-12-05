#Advent of Code 2020 - Day 2
import sys
sys.path.append('/home/trackback/Desktop/AoC-2020')
from Utilities import read_list
import re

input_list = read_list(2)
input_list_test = read_list(2, 'test')

def verify_password(list):
	answer, answer_2 = [], []

	for line in input_list:
		pol_min, pol_max, letter, ignore, password = re.split(r"[-: ]", line)
		pol_min, pol_max = map(int, [pol_min, pol_max])

		if password.count(letter) in range(pol_min, pol_max+1):
			answer.append(password)

		if password[pol_min-1] == letter and password[pol_max-1] == letter:
			continue
		elif password[pol_min-1] == letter or password[pol_max-1] == letter:
			answer_2.append(password)

	return len(answer), len(answer_2)

print (verify_password(input_list))