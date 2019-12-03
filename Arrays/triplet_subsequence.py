# triplet_subsequence.py
from bisect import bisect_left

def tripletSubsequence(arr):
    '''
    if arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 return true,
    else return false
    '''

    triplet = [float('inf')]*2

    for num in arr:
        index = bisect_left(triplet, num)
        print(index, triplet, num)

        # if index to be inserted is at index 2 or higher, return True
        if index >= 2:
            return True
        triplet[index] = num

    return False





print(tripletSubsequence([5,1,5,5,2,5,4])) # Expected: true
