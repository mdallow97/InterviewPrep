# 5_2
# First bad version

bad = 1702766719
def isBadVersion(version):
	return version >= bad

def firstBadVersion(n):
	if n == 1:
		return 1
	mid = n/2
	prev_mid = 0

	while mid > 0 and mid < n:
		if isBadVersion(mid):
			if not isBadVersion(mid-1):
				return mid
			else:
				mid -= (mid-prev_mid)/2
				continue
		else:
			if isBadVersion(mid+1):
				return mid+1
			else:
				print(mid, mid+(n-mid)/2)
				prev_mid = mid
				mid += (n-mid)/2
				continue

	return mid



print(firstBadVersion(2126753390))