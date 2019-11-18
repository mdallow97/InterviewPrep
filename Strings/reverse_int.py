# 2_2
# Reverse integer

def reverse(x):
	s = str(x)
	result = 0
	if x < 0:
		result_str = s[1:len(s)]
		result = int(result_str[::-1])*-1
	else:
		result = int(s[::-1])

	if result > 2147483647:
		return 0
	elif result < -2147483648:
		return 0
	else:
		return result

print(reverse(-70))