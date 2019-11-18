# 4_4
# Binary tree level order traversal

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def levelOrder(root):

	if not root:
		return []
	
	order = []
	queue = []
	queue.append([root, 0])

	while len(queue) > 0:
		cursor,height = queue.pop(0)
		print(cursor.val)
		order.append([cursor,height])

		if cursor.left:
			queue.append([cursor.left, height+1])

		if cursor.right:
			queue.append([cursor.right, height+1])

	dic = {}
	for node,height in order:
		if height in dic:
			dic[height].append(node.val)
		else:
			dic[height] = [node.val]

	result = []
	for key in sorted(dic.keys()):
		result.append(dic[key])

	return result




root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(levelOrder(None))