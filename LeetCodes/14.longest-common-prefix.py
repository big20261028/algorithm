#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs.pop()
        prefix_len = len(result)
        for str in strs:
            cnt = 0
            for idx, char in enumerate(str):
                if len(result) <= idx or result[idx] != char:
                    break
                cnt += 1
            prefix_len = min(prefix_len, cnt)
            if prefix_len == 0:
                return ""
        
        result = result[:prefix_len]
        return result
            
        
# @lc code=end

