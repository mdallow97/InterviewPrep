# 4_5
# Convert sorted array to binary search tree

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def sortedArrayToBST(nums):
	if len(nums) == 0:
		return None
	elif len(nums) == 1:
		return TreeNode(nums[0])

	mid = len(nums)/2
	node = TreeNode(nums[mid])

	node.left = sortedArrayToBST(nums[0:mid])
	node.right = sortedArrayToBST(nums[mid+1:len(nums)])
	return node




print(sortedArrayToBST([-10,-3,0,5,9]))