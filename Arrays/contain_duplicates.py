# 1_4
# Contains duplicates

from collections import defaultdict

def containsDuplicate(nums):
	if len(set(nums)) < len(nums):
		return True
	else:
		return False


print(containsDuplicate([1,2,3,4,5]))
