# 2_3
# First unique character in a string

def firstUniqChar(s):
	if len(s) == 1:
		return 0

	for i,c in enumerate(s):
		print(c)
		if c in s[i+1:len(s)] or c in s[0:i]:

			continue
		else:
			return i

	return -1

def firstUniqChar2(s):
	dic = {}

	for c in s:
		if c in dic:
			dic[c] += 1
		else:
			dic[c] = 1

	for i,c in enumerate(s):
		if dic[c] == 1:
			return i

	return -1



print(firstUniqChar2("c"))