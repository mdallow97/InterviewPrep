# serialize.py

class BTnode:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


def inOrderConstruction(root, node_list):
	if not root:
		node_list.append(None)
		return

	node_list.append(root.value)
	inOrderConstruction(root.left, node_list)
	inOrderConstruction(root.right, node_list)

def serialize(root):
	node_list = []
	inOrderConstruction(root, node_list)
	return node_list


def inOrderDeconstruction(root, node_list):
	if not node_list:
		return

	node = node_list.pop(0)

	if node == None:
		return

	root = BTnode(node)
	root.left = inOrderDeconstruction(root.left, node_list)
	root.right = inOrderDeconstruction(root.right, node_list)

	return root

def deserialize(node_list):
	if len(node_list) == 0:
		return None
	root = BTnode(node_list.pop(0))
	root.left = inOrderDeconstruction(root.left, node_list)
	root.right = inOrderDeconstruction(root.right, node_list)

	return root



root = BTnode(1)
root.left = BTnode(2)
root.right = BTnode(3)

cursor = root.right
cursor.left = BTnode(4)
cursor.right = BTnode(5)


print(serialize(root))
print(serialize(deserialize(serialize(root))))
print(serialize(deserialize([1,2,None,None,3,4,None,None,5,None,None])))
print(serialize(deserialize([1,0,-1])))