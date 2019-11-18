# 2_1
# Reverse string

def reverseString(s):
	for i in range(len(s)):
		j = (len(s)-1) - i

		if j <= i:
			break

		temp = s[j]
		s[j] = s[i]
		s[i] = temp

def reverseString2(s):
	s = s.reverse()

s = ["H","a","n","n","a","h"]
reverseString2(s)
print(s)