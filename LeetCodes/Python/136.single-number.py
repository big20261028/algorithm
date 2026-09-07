#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sum_max_val = sum(set(nums)) * 2
        sum_val = sum(nums)
        result = sum_max_val - sum_val
        return result
        # print(nums[0])

# @lc code=end

