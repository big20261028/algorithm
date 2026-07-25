#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first_idx in range(len(nums)):
            for second_idx in range((first_idx + 1), len(nums)):
                first_num = nums[first_idx]
                second_num = nums[second_idx]
                if first_num + second_num == target:
                    return [first_idx, second_idx]
            
        
# @lc code=end

