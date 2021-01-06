# kth_largest_element.py

def findKthLargest(nums, k):
	nums.sort()
	return nums[len(nums) - k]

def main():
	print(findKthLargest([3,2,1,5,6,4], 2))

if __name__ == "__main__":
	main()