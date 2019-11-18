# 1_8
# Move zeroes

def moveZeroes(nums):
	i = 0
	num_zeroes = 0
	while i < len(nums):
		print(i,":",nums)
		if i + num_zeroes == len(nums):
			break
		elif nums[i] == 0:
			nums.pop(i)
			nums.append(0)
			num_zeroes += 1
		else:
			i+=1


nums = [0,0,1]
moveZeroes(nums)
print(nums)
