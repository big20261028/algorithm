#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start

class Solution:
    def romanToInt(self, s: str) -> int:
        flag = False
        
        symbol_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        result = 0
        
        for idx in range(len(s) - 1):
            if flag:
                flag = False
                continue    
            
            current_num = symbol_dict[s[idx]]
            next_num = symbol_dict[s[idx+1]]
            
            if current_num < next_num:
                flag = True
                result += next_num - current_num
            else:
                result += current_num
        
        if not flag:
            result += symbol_dict[s[-1]]  
        
        return result        
        
# @lc code=end

