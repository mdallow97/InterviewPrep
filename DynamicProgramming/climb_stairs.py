# 6_1
# Climbing stairs
stairs = {}

def climbStairs(n):
	if n == 1:
		return 1
	elif n == 2:
		return 2

	stairs[n-2] = climbStairs(n-2)
	if n-1 in stairs:
		return stairs[n-1] + stairs[n-2]
	else:
		return climbStairs(n-1) + stairs[n-2]



print(climbStairs(4))