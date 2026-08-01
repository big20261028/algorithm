#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        target_idx = 0
        # cnt = 0
        for num in nums:
            if num != val:
                nums[target_idx] = num
                target_idx += 1
        return target_idx

# @lc code=end

