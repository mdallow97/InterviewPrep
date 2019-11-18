# 4_2
# Validate binary search tree

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def left_utility(root):
	if not root:
		return -2**31-1
	
	mx = max(left_utility(root.left), left_utility(root.right))
	if mx > root.val:
		return mx
	else:
		return root.val


def right_utility(root):
	if not root:
		return 2**31

	mn = min(right_utility(root.left), right_utility(root.right))
	if mn < root.val:
		return mn
	else:
		return root.val

def isValidBST(root):

	if not root:
		return True

	return ((root.val > left_utility(root.left)) and isValidBST(root.left)) and ((root.val < right_utility(root.right)) and isValidBST(root.right))


def isValidBST2(root):
	def helper(node, lower, upper):
		if not node:
			return True

		# Check self
		if node.val <= lower or node.val >= upper:
			return False

		# Check left subtree
		if not helper(node.left, lower, node.val):
			return False

		# Check right subtree
		if not helper(node.right, node.val, upper):
			return False

		return True

	return helper(root, -float("inf"), float("inf"))
		



root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)


print(isValidBST2(root))