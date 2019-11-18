# 2_8
# Count and say

def countAndSay(n):
	if n < 1:
		return "0"
	elif n == 1:
		return "1"

	result = ""
	prev = countAndSay(n-1)
	i = 0

	while i < len(prev):
		count = 1
		while i+count < len(prev) and prev[i] == prev[i+count]:
			count += 1
		result += str(count)+prev[i]
		i += count

	return result



print(countAndSay(4))