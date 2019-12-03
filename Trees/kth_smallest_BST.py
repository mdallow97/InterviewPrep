# kth_smallest_BST.py

class BSTnode:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

def preOrder(root, node_list):
	if not root:
		return

	node_list.append(root.value)
	preOrder(root.left, node_list)
	preOrder(root.right, node_list)

def findKthSmallest(root, k):
	node_list = []
	preOrder(root, node_list)
	node_list.sort()

	return node_list[k-1]

def findKthSmallest2(root, k):
	if not root:
		return 0

	stack = []

	while stack or root:
		while root:
			stack.append(root)
			root = root.left

		l = [node.value for node in stack]
		print(l)
		root = stack.pop()
		k -= 1
		if k == 0:
			return root.value

		root = root.right
		if root:
			print(root.value)




root = BSTnode(5)
cursor = root

cursor.left = BSTnode(3)
cursor.right = BSTnode(6)
cursor = cursor.left

cursor.left = BSTnode(2)
cursor.right = BSTnode(4)
cursor.left.left = BSTnode(1)


print(findKthSmallest2(root, 4))
