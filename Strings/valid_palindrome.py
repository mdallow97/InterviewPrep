# 2_5
# Valid Palindrome

def isPalindrome(s):
	edited = ""
	for c in s.lower():
		if c.isalnum():
			edited += c

	print(edited)
	if edited == edited[::-1]:
		return True
	else:
		return False
	


print(isPalindrome("A man, a plan, a canal: Panama"))