# 7_1
# Shuffle an array

import random

class Solution(object):
	def __init__(self, nums):
		self.original = nums[:]
		self.scrambled = nums[:]

	def reset(self):
		self.scrambled = self.original[:]
		return self.scrambled

	def shuffle(self):
		if len(self.original) == 0:
			return []

		pos = {}
		pos[0] = random.randint(0, len(self.scrambled)-1)

		i = 1
		while i < len(self.scrambled):
			rand = random.randint(0, len(self.scrambled)-1)
			for key in pos.keys():
				if pos[key] == rand:
					break
			else:
				pos[i] = rand
				i += 1


		print(pos)
		for i in range(len(self.scrambled)):

			self.scrambled[i] = self.original[pos[i]]

		return self.scrambled

	def shuffle1(self):
		copy = self.scrambled[:]

		for i in range(len(self.scrambled)):
			rand = random.randint(0, len(copy)-1)
			self.scrambled[i] = copy.pop(rand)

		return self.scrambled

	def shuffle2(self):
		random.shuffle(self.scrambled)
		return self.scrambled


obj = Solution([1,2,3])
print(obj.reset())
print(obj.shuffle2())
print(obj.reset())
print(obj.shuffle2())