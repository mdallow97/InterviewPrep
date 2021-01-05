def isPalindrome(x):
	if x < 0:
		return False

	num = str(x)
	l = 0
	r = len(num) - 1

	while l < r:
		if not num[l] == num[r]:
			return False

		l += 1
		r -= 1

	return True



def main():
	print(isPalindrome(-222))

if __name__ == "__main__":
	main()