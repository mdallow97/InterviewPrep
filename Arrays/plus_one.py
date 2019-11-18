# 1_7
# Plus one

def plusOne(digits):
	my_string = ""
	for item in digits:
		my_string += str(item)

	temp = str(int(my_string) + 1)

	result = []
	for c in temp:
		result.append(int(c))

	return result

print(plusOne([4,3,2,1]))