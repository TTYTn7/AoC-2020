#Advent of Code 2020 - Day 4
import re

def get_input(file):
	passports = []
	with open(file, 'r') as f:
		all_passports = f.read().strip()

		for passport in all_passports.split('\n\n'):
			passport_dict = {}

			for item in re.split(r'[\s]', passport):
				key, value = item.split(':')
				passport_dict[key] = value

			passports.append(passport_dict)

	return passports

passports = get_input('day4_input.txt')
#passports_test = get_input('day4_test.txt')

def day4(input_val):
	required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
	total = 0

	for passport in input_val:
		if all(item in passport.keys() for item in required):
			is_valid = True

			if int(passport['byr']) not in range(1920, 2003) or int(passport['iyr']) not in range(2010, 2021) or int(passport['eyr']) not in range(2020, 2031):
				is_valid = False

			re_pts = [r'^\d{9}$', r'^#[0-9a-f]{6}$', r'^amb|blu|brn|gry|grn|hzl|oth$']
			if not re.match(re_pts[0], passport['pid']) or not re.match(re_pts[1], passport['hcl']) or not re.match(re_pts[2], passport['ecl']):
				is_valid = False
			

			if not re.match(r'^1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in$', passport['hgt']):
				is_valid = False

			# if passport['hgt'][-2:] == 'cm':
			# 	if int(passport['hgt'][:-2]) not in range(150, 194):
			# 		is_valid = False
			# elif passport['hgt'][-2:] == 'in':
			# 	if int(passport['hgt'][:-2]) not in range(59, 77):
			# 		is_valid = False
			# else:
			# 	is_valid = False

			if is_valid:
				total += 1 
		

	return 'done', total

#print (day4(passports_test))
print (day4(passports))