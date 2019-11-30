# find_median.py
import bisect

class MedianFinder(object):
    def __init__(self):
        # init data structure
        self.nums = []

    def addNum(self, num):
        # add new number
        bisect.insort(self.nums, num)

    def findMedian(self):
        if not self.nums:
            return 0

        index = int(len(self.nums)/2)
        print(index)
        if len(self.nums) % 2 == 0:
            return (float(self.nums[index-1]) + float(self.nums[index])) / 2.0
        else:
            return float(self.nums[index])


obj = MedianFinder()
obj.addNum(2)
obj.addNum(4)
obj.addNum(1)
obj.addNum(6)

print(obj.findMedian())
