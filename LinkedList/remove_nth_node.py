# 3_2
# Remove nth node from end of list

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def printList(self):
		cursor = self
		while cursor != None:
			print(cursor.val)
			cursor = cursor.next


def removeNthNodeFromEnd(head, n):
	if head.next == None:
		return None

	prev_cursor1 = head
	prev_cursor2 = head
	cursor = head
	count = 0

	while cursor != None:
		if count >= n:
			prev_cursor2 = prev_cursor1
			prev_cursor1 = prev_cursor1.next

		cursor = cursor.next
		count += 1

	if prev_cursor1.next != None:
		prev_cursor1.val = prev_cursor1.next.val
		prev_cursor1.next = prev_cursor1.next.next
	else:
		prev_cursor2.next = None
	

	return head


ll = ListNode(1)
cursor = ll

cursor.next = ListNode(2)
cursor = cursor.next

cursor.next = ListNode(3)
cursor = cursor.next

cursor.next = ListNode(4)
cursor = cursor.next

cursor.next = ListNode(5)

ll = removeNthNodeFromEnd(ll, 1)
ll.printList()