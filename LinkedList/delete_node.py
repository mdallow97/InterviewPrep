# 3_1
# Delete node in a linked list

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def printList(self):
		cursor = self
		while cursor != None:
			print(cursor.val)
			cursor = cursor.next


def deleteNode(node):
	node.val = node.next.val
	node.next = node.next.next

ll = ListNode(4)
cursor = ll

remove = cursor.next = ListNode(5)
cursor = cursor.next

cursor.next = ListNode(1)
cursor = cursor.next

cursor.next = ListNode(9)


deleteNode(remove)
ll.printList()
