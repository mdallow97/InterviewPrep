# median_two_arrays.py
def median_two_arrays(nums1, nums2):
    nums1 += nums2
    nums1.sort()

    if not nums1:
        return 0

    index = int(len(nums1)/2)
    if len(nums1) % 2 == 0:
        return (float(nums1[index-1]) + float(nums1[index])) / 2.0
    else:
        return float(nums1[index])


print(median_two_arrays([], [2]))
