#Advent of Code reading input
import requests

def read_list(day, test=False):
	day = str(day)

	if not test:
		file = "day"+day+"_input.txt"
	else:
		file = "day"+day+"_test.txt"

	input_list = []

	with open(file, 'r') as f:
		line = f.readline()
		while line:
			try:
				input_list.append(int(line))
			except:
				input_list.append(line.strip())
			line = f.readline()

	return input_list

def get_input(day):
	day = str(day)
	input_link_default = "https://adventofcode.com/2020/day/"
	daily_input_link = input_link_default+day+"/input"
	daily_input_file_name = "day"+day+"_input.txt"
	
	content = requests.get(daily_input_link)

	with open(daily_input_file_name, 'w') as file:
		file.write(content.text)

	return None