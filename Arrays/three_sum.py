# 1_1
# 3Sum

def twoSum(nums, target, skip, combos):
	dic = {}
	for i,num in enumerate(nums):
		if skip == i or num in combos:
			continue

		if target - num not in dic:
			dic[num] = i
		else:
			return dic[target-num], i

	return -1,-1
		

def threeSum(nums):
	result = []
	for i,num in enumerate(nums):
		x = num
		y,z = twoSum(nums, -x, i, [])
		combos = []
		while y >= 0 and z >= 0:

			if nums[y] + nums[z] == -x:
				new_combo = [x,nums[y],nums[z]]
				new_combo.sort()

				if new_combo not in result:
					result.append(new_combo)

			combos.append(nums[y])
			y,z = twoSum(nums, -x, i, combos)

	return result

def threeSum2(nums):
	result = []
	nums.sort()

	for i in range(len(nums)-2):
		if i > 0 and nums[i] == nums[i-1]:
			continue
		l,r = i+1,len(nums)-1
		while l < r:
			sm = nums[i] + nums[l] + nums[r]

			if sm < 0:
				l += 1
			elif sm > 0:
				r -= 1
			else:
				result.append([nums[i], nums[l], nums[r]])
				while l < r and nums[l] == nums[l+1]:
					l += 1

				while l < r and nums[r] == nums[r-1]:
					r -= 1

				l += 1
				r -= 1
		return result


print(threeSum2([-1,0,1,2,-1,-4]))











