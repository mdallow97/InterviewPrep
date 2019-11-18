# 2_9
# Longest common prefix

def longestCommonPrefix(strs):
	result = ""
	if len(strs) is 0:
		return ""

	for i in range(len(strs[0])):
		for item in strs:
			if i >= len(item) or not item[i] == strs[0][i]:
				return result
		else:
			result += strs[0][i]

	return result

		 
print(longestCommonPrefix(["aa", "a"]))