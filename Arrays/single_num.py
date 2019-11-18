# 1_5
# Single number

def singleNumber(nums):
	nums.sort()

	i = 0
	while i < len(nums)-1:
		if nums[i] == nums[i+1]:
			i+=2
			continue
		else:
			return nums[i]

	return nums[i]


print(singleNumber([4,1,2,1,2]))