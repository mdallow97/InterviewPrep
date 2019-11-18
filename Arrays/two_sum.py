# 1_9
# Two sum

def twoSum(nums, target):
	index = None
	for i in range(len(nums)-1):
		value = target - nums[i]
		copy = nums[i+1:len(nums)]
		try:
			index = copy.index(value)+i+1
		except:
			continue

		if index == i:
			index = None
			continue 
		elif not index == None:
			break


	return [i, index]

def twoSum2(nums, target):
	dic = {}
	for i,num in enumerate(nums):
		if target-num not in dic:
			dic[num] = i
		else:
			return [dic[target-num], i]

nums = [7, 10, 12, -1]

print(twoSum2(nums, 6))
