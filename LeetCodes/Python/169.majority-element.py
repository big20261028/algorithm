#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # array_len = len(nums)
        # sum_val = sum(nums)
        # if array_len <= 1:
        #     result = sum_val
        # else:
        #     if sum_val % array_len:
        #         result = sum(nums) // array_len + 1
        #     else:
        #         result = sum(nums) // array_len
        candidate_num = None
        cnt = 0

        for num in nums:
            # print(candidate_num, cnt)
            if not cnt:
                candidate_num = num
                cnt = 1
            elif candidate_num == num:
                cnt += 1
            else:
                cnt -= 1

        return candidate_num
        
# @lc code=end

