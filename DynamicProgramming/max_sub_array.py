# 6_3
# max sub array

def maxSubArray(nums):
	result = -99999999
	size = len(nums)
	while size > 0:
		i = 0
		while i + size < len(nums)+1:
			mx = 0
			for num in nums[i:i+size]:
				mx += num

			if mx > result:
				result = mx

			i += 1
		size -= 1

	return result

def maxSubArray2(nums):
	max_so_far = -99999999
	max_ends = 0

	for i in range(len(nums)):
		max_ends = max_ends + nums[i]

		if max_so_far < max_ends:
			max_so_far = max_ends
		if max_ends < 0:
			max_ends = 0
	return max_so_far



print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

