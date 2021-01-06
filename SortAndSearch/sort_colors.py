# sort_colors.py

def sortColor(nums):
	rwb = [0, 0, 0]

	for num in nums:
		rwb[num] += 1

	print(nums)
	nums[0:rwb[0]] = [0 for zero in range(rwb[0])]
	nums[rwb[0]:rwb[0]+rwb[1]] = [1 for one in range(rwb[1])]
	nums[rwb[0]+rwb[1]:len(nums)] = [2 for twos in range(rwb[2])]
	print(nums)


def main():
	sortColor([1])

if __name__ == "__main__":
	main()