# 3_4
# Merge two sorted linked list

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def printList(self):
		cursor = self
		while cursor != None:
			print(cursor.val)
			cursor = cursor.next

def mergeTwoLists(l1, l2):
	if l1 == None:
		return l2
	elif l2 == None:
		return l1



	new = None
	if l1.val < l2.val:
		new = ListNode(l1.val)
		l1 = l1.next
	else:
		new = ListNode(l2.val)
		l2 = l2.next

	cur = new

	while l1 != None and l2 != None: # will stop when one list is empty

		if l1.val < l2.val:
			cur.next = ListNode(l1.val)
			l1 = l1.next
		else:
			cur.next = ListNode(l2.val)
			l2 = l2.next

		cur = cur.next

	rest = None
	if l1 != None:
		rest = l1
	elif l2 != None:
		rest = l2
	else:
		return new

	while rest != None:
		cur.next = ListNode(rest.val)
		rest = rest.next
		cur = cur.next

	return new


# Faster!
def mergeTwoLists2(l1, l2):
	ll = []

	while l1:
		ll.append(l1.val)
		l1 = l1.next
	while l2:
		ll.append(l2.val)
		l2 = l2.next

	ll.sort()
	node = None
	first = None

	for item in ll:
		if node:
			node.next = ListNode(item)
			node = node.next
		else:
			node = ListNode(item)
			first = node

	return first

l1 = ListNode(1)
cursor1 = l1

cursor1.next = ListNode(3)
cursor1 = cursor1.next

cursor1.next = ListNode(5)

l2 = ListNode(1)
cursor2 = l2

cursor2.next = ListNode(1)
cursor2 = cursor2.next

cursor2.next = ListNode(4)

new = mergeTwoLists2(None, None)
new.printList()





