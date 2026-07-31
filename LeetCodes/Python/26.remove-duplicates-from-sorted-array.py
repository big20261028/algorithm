#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        target_idx = 1
        target_num = nums[0]
        for i in range(1, len(nums)):
            if target_num < nums[i]:
                nums[target_idx] = nums[i]
                target_idx += 1
                target_num = nums[i]

        return target_idx

# @lc code=end

