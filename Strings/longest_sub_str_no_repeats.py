# 1_4
# Longest substring without repeating character

def longestSubstring(s):
	i = 0
	mx = 0
	sub = ""
	while i < len(s):
		c = s[i]
		if c in sub:


			mx = max(mx, len(sub))
			i = (i - len(sub)) + sub.index(c) + 1
			sub = ""
			continue

		sub += c
		i += 1


	return mx


def longestSubstring2(s):
	seen = {}
	mx = 0
	start = 0

	for i, c in enumerate(s):
		if c in seen and start <= seen[c]:
			start = seen[c]+1
		else:
			mx = max(mx, i-start+1)

		seen[c] = i

	return mx

print(longestSubstring2("pwwkew"))
