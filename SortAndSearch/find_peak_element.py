# find_peak_element.py

def findPeakElement(nums):
	if len(nums) == 1:
		return 0
	elif nums[0] > nums[1]:
		return 0
	elif nums[len(nums)-1] > nums[len(nums)-2]:
		return len(nums)-1

	for i in range(1, len(nums)-1):
		if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
			return i

def main():
	print(findPeakElement([1,2,1,3,5,6,4]))

if __name__ == "__main__":
	main()