#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for idx, num in enumerate(nums):
            if target <= num:
                return idx

        return len(nums)

        
# @lc code=end

