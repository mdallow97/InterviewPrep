# 3_3
# Reverse linked list

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def printList(self):
		cursor = self
		while cursor != None:
			print(cursor.val)
			cursor = cursor.next


def revListRec(head):
	if head.next == None or head == None:
		return head

	rest = revListRec(head.next)
	head.next.next = head
	head.next = None

	return rest


def reverseList(head):
	if head == None or head.next == None:
		return head

	rest = reverseList(head.next)
	head.next.next = head
	head.next = None

	return rest


def revListIter1(head):
	prev = None
	cur = head

	while cur != None:
		nxt = cur.next
		cur.next = prev
		prev = cur
		cur = nxt

	return prev

def revListIter2(head):
	ll = []
	while head:
		ll.append(head.val)
		head = head.next

	print(ll)

	node = None
	first = None
	for item in reversed(ll):
		if node:
			node.next = ListNode(item)
			node = node.next
		else:
			node = ListNode(item)
			first = node

	return first


ll = ListNode(1)
cursor = ll

cursor.next = ListNode(2)
cursor = cursor.next

cursor.next = ListNode(3)
cursor = cursor.next

cursor.next = ListNode(4)
cursor = cursor.next

cursor.next = ListNode(5)

ll = revListIter2(ll)
ll.printList()