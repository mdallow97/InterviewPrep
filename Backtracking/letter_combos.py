# 4_1
# Letter combinations of a phone number

nums = {
	2: ['a','b','c'],
	3: ['d','e','f'],
	4: ['g','h','i'],
	5: ['j','k','l'],
	6: ['m','n','o'],
	7: ['p','q','r','s'],
	8: ['t','u','v'],
	9: ['w','x','y','z']
}

def letterCombinations(digits):
	num_combos = 0
	result = []



	for digit in digits:
		# len(result) == len(result) * len(nums(int(digit)))
		letters = nums[int(digit)]
		if len(result) == 0:
			result = letters
		else:
			result = [letter for letter in result for i in range(len(nums[int(digit)]))]
			for i,s in enumerate(result):
				result[i] += nums[int(digit)][i%len(nums[int(digit)])]


	return result




print(letterCombinations("27"))