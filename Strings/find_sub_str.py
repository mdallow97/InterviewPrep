# 2_7
# Implement strStr()

def strStr(haystack, needle):
	if needle == "":
		return 0

	try:
		return haystack.index(needle)
	except:
		return -1


def strStr1(haystack, needle):
	if needle == "":
		return 0
	elif needle not in haystack:
		return -1

	index = -1

	for i,c in enumerate(haystack):
		if c == needle[0]:
			if haystack[i:i+len(needle)] == needle:
				index = i
				break

	return index



haystack = "hello there"
needle = "th"
print(strStr1(haystack, needle))