def divide(dividend, divisor):
	print(dividend, " / ", divisor)
	quotient = 0
	remainder = 0
	if not divisor == 1:
		while dividend >= divisor:
			dividend -= divisor
			quotient += 1
		remainder = dividend

	else:
		quotient = dividend

	return quotient, remainder


def long_division(dividend, divisor):
	top = abs(dividend)
	bottom = abs(divisor)

	div_str = str(top)
	quo_str = ""

	i = 0
	rem = 0

	if not bottom == 1:
		while i < len(div_str):
			new_div = int(str(rem) + str(0)) + int(div_str[i])
			quo, rem = divide(new_div, bottom)
			quo_str += str(quo)

			i += 1

	else:
		quo_str = str(top)

	if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0):
		if int(quo_str) == 2147483648:
			return int(quo_str) - 1
		return int(quo_str)
	else:
		return (0 - int(quo_str))


def main():
	print(long_division(10, 3))

if __name__ == "__main__":
	main()