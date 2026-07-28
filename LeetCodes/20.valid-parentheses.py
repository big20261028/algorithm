#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    str_dict = {
        "(" : ")",
        "{" : "}",
        "[" : "]"
    }
    
    def isValid(self, s: str) -> bool:
        stack = []
        idx = 0
        while idx < len(s):
            target_char = s[idx]
            
            if target_char in self.str_dict:
                stack.append(target_char)  
            else:
                if not stack:
                    return False
                
                pop_char = stack.pop()
                if self.str_dict[pop_char] != target_char:
                    return False
            idx += 1
        
        if stack:
            return False
        else:
            return True
        
        
        
# @lc code=end

