import sys

def get_largest_tidy(num_str):
	# print(num_str)
	digits = [int(x) for x in list(num_str)]
	return fix_digits(digits)

def check_tidy(digits):
	return digits == sorted(digits)

def fix_digits(digits):
	while not check_tidy(digits):
		digits = one_pass(digits)
	return ''.join([str(x) for x in digits]).lstrip('0')

def one_pass(digits):
	for i, digit in enumerate(digits[:-1]):
		if digit > digits[i+1]:
			digits[i] -= 1
			digits[i+1:] = [9]*(len(digits) - i - 1)
			return digits
	return digits


def read_and_write(file_name):
	with open(file_name) as f:
		next(f)
		case = 1
		for line in f:
			result = get_largest_tidy(line.strip())
			print('Case #{case}: {result}'.format(case=case, result=result))
			case += 1

read_and_write(sys.argv[1])
