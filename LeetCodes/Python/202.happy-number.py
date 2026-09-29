#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        one_step_pointer = n
        two_step_pointer = n
        
        while True:
            one_step_pointer = self.getVal(one_step_pointer)
            two_step_pointer = self.getVal(self.getVal(two_step_pointer))
            
            if two_step_pointer == 1:
                return True

            if one_step_pointer == two_step_pointer:
                return False
            
        
    def getVal(self, number):
        
        total = 0
        while number > 0:
            val = number % 10
            total += val ** 2
            number //= 10
        return total
        
# @lc code=end

