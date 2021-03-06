# insertion_sort.py
from random import sample, seed

class ListNode():
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
	
	def constructFromList(self, l):
		head = ListNode(l.pop(0))
		cursor = head
		for e in l:
			cursor.next = ListNode(e)
			cursor = cursor.next

		self.val = head.val
		self.next = head.next

	def printList(self):
		cursor = self
		while cursor:
			if cursor.next:
				end = '->'
			else:
				end = '\n'
			print(cursor.val, end=end)
			cursor = cursor.next

	def insertionSort(self):
		sortedLL = None
		head = self
		while head:
			node_insert = head.val
			head = head.next

			if not sortedLL:
				sortedLL = ListNode(node_insert)
				continue

			cursor = sortedLL
			if sortedLL.val > node_insert:
				sortedLL = ListNode(node_insert, next=sortedLL)
				continue

			while cursor:
				if not cursor.next:
					cursor.next = ListNode(node_insert)
					break
			    
				if cursor.val <= node_insert and node_insert <= cursor.next.val:
					temp = cursor.next
					cursor.next = ListNode(node_insert, next=temp)
					break
				
				cursor = cursor.next
			   
		self.val = sortedLL.val
		self.next = sortedLL.next

	def fastSort(self):
		l = []
		head = self
		while head:
			l.append(head.val)
			head = head.next

		self.constructFromList(sorted(l))

def main():
	l = [4,2,1,3]
	ll = ListNode()
	ll.constructFromList(l)
	ll.insertionSort()
	ll.printList()

	seed(0)
	l = sample(range(-1024, 1024), 128)
	ll.constructFromList(l)
	ll.fastSort()
	ll.printList()

if __name__ == '__main__':
	main()