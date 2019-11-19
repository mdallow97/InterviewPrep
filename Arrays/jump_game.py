# jump game

def canJump(nums):
	if len(nums) == 1:
		return True

	prev = []
	for i,num in enumerate(nums):
		if num == 0:
			# search prev array for jump to pass it (or equal if last element)
			# need prev[j] + j > i
			for j in range(len(prev)):
				if i == len(nums)-1 and prev[j] + j >= i:
					break
				elif prev[j] + j > i:
					break
			else:
				return False

		prev.append(num)

	return True


print(canJump([3,2,1,0,4]))