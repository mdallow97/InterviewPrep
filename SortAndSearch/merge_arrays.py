# 5_1
# Merge sorted array

def merge(nums1, m, nums2, n):
	for i,item in enumerate(nums2):
		nums1[len(nums1)-len(nums2)+i] = item
	nums1.sort()


def swap(a,b, nums):
	temp = nums[a]
	nums[a] = nums[b]
	nums[b] = temp
	return nums

def merge2(nums1, m, nums2, n):
	for i in range(n):
		nums1[m] = nums2[i]
		for j in range(m):
			if nums2[i] <= nums1[j]:
				break
		else:
			j = m

		print("swap from", j, "to", m)
		k = m
		while k > j:
			nums1 = swap(k, k-1, nums1)
			k -= 1

		m += 1




nums1 = [4,7,8,0,0,0]
nums2 = [1,2,5]
merge2(nums1, 3, nums2, 3)
print(nums1)
