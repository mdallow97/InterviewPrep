// binarySearch.cpp

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int offset = 0;
        while (nums.size() > 0) {
            int index = nums.size() / 2;
            
            if (target == nums[index])
                return index + offset;
            else if (target < nums[index]) {
                // Resize array (erase upper half)
                nums.erase(nums.begin()+index, nums.end());
            } else if (target > nums[index]) {
                // Resize array (erase lower half)
                if (index == 0)
                    nums.erase(nums.begin());
                else nums.erase(nums.begin(), nums.begin() + index);
                offset += index;
            } else return -1;
        }
        return -1;
    }
};