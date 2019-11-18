# 2_6
# String to integer

def myAtoi(s):
	if s == '':
		return 0

	num = ""
	sign = 1
	has_sign = False
	for c in s:

		if c == '+' or c == '-' or c == ' ':
			if len(num) > 0 or has_sign:
				break
			
			if c == '-':
				sign = -1
				has_sign = True
			elif c == '+':
				has_sign = True

		elif not c.isdigit():
			break
		else:
			num += c

	if num == "":
		return 0
	result = int(num) * sign

	if result > (2**31) - 1:
		return (2**31)-1
	elif result < -2**31:
		return -2**31
	else:
		return result


print(myAtoi("+ 2"))