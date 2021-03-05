def isValid(s):
	brackets = {
	'(': ')',
	'[': ']',
	'{': '}'
	}

	stack = []
	for c in s:
		if c in brackets:
			stack.append(brackets[c])
		elif len(stack) > 0 and c == stack[len(stack)-1]:
			stack.pop(len(stack)-1)
		else:
			return False

	if len(stack) == 0:
		return True
	else:
		return False

def main():
	print(isValid("()"))
	print(isValid("()[]{}"))
	print(isValid("(]"))
	print(isValid("([)]"))
	print(isValid("{[]}"))

if __name__ == '__main__':
	main()