#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        size = len(digits) - 1
        new_num = 0
        for i in range(len(digits)):
            new_num += 10**size * digits[i]
            size -= 1
        new_num += 1
        new_str = str(new_num)
        result = []
        for j in range(len(new_str)):
            result.append(int((new_str[j])))
        return result




        
        
            
        
        
# @lc code=end

