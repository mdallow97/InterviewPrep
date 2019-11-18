# 3_5
# Palindrome linked list

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def printList(self):
		cursor = self
		while cursor != None:
			print(cursor.val)
			cursor = cursor.next


def isPalindrome(head):
	ll = []
	while head:
		ll.append(head.val)
		head = head.next

	return ll == ll[::-1]



ll = ListNode(1)
cursor = ll

cursor.next = ListNode(2)
cursor = cursor.next

cursor.next = ListNode(2)
cursor = cursor.next

cursor.next = ListNode(1)
cursor = cursor.next

cursor.next = ListNode(1)

print(isPalindrome(ll))