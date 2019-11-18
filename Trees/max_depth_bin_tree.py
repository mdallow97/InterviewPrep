# 4_1
# Max depth of binary tree

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

	def printList(self):
		cursor = self
		while cursor != None:
			print(cursor.val)
			cursor = cursor.next


count = 1
cl = []
def maxDepth(root):
	global count
	print(count, "at", root.val)

	if not root:
		return 0

	elif not root.left and not root.right:
		cl.append(count)
		count = 1 + len(cl)
		return max(cl)

	count += 1
	if root.left:
		maxDepth(root.left)

	if root.right:
		maxDepth(root.right)

	return max(cl)

def maxDepth2(root):
	if not root:
		return 0

	return max(maxDepth2(root.left), maxDepth2(root.right)) + 1





root = TreeNode(0)
root.left = TreeNode(9)
root.left.left = TreeNode(10)
root.left.left.left = TreeNode(11)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.left.left = TreeNode(16)
root.right.right = TreeNode(7)

print(maxDepth2(root))