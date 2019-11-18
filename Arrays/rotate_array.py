# 1_3
# Rotate array

def rotate(nums, k):
	if k > len(nums):
		k = k%len(nums)

	nums.reverse()
	nums[0:k] = nums[0:k][::-1]
	nums[k:len(nums)] = nums[k:len(nums)][::-1]

nums = [1,2]
rotate(nums, 3)
print(nums)
