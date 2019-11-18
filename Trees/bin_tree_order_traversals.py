# 3_1
# binary tree inorder traversal

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def in_helper(root, ll):
	if not root:
		return

	if root.left:
		in_helper(root.left, ll)

	ll.append(root.val)

	if root.right:
		in_helper(root.right, ll)

def inorderTraversal(root):
	ll = []
	in_helper(root, ll)
	return ll


def preorderTraversal(root):
	if not root:
		return

	print(root.val)

	if root.left:
		preorderTraversal(root.left)

	if root.right:
		preorderTraversal(root.right)

def postorderTraversal(root):
	if not root:
		return

	if root.left:
		postorderTraversal(root.left)

	if root.right:
		postorderTraversal(root.right)

	print(root.val)



root = TreeNode(1)
cursor = root

cursor.left = TreeNode(2)
cursor.right = TreeNode(3)

cursor = cursor.left
cursor.left = TreeNode(4)
cursor.right = TreeNode(5)

print(inorderTraversal(root))