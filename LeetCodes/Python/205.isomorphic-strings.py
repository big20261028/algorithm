#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_length = len(s)
        if char_length != len(t):
            return False
        
        char_dict = dict()
        matched_char = set()
        
        for idx in range(char_length):
            s_char = s[idx]
            t_char = t[idx]
            
            if s_char in char_dict:
                if char_dict[s_char] != t_char:
                    return False
            else:
                if t_char in matched_char:
                    return False
                char_dict[s_char] = t_char
                matched_char.add(t_char)
        
        return True
            
            
        
        
        
# @lc code=end

