#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest_str_len = 0
        cur_text = ""
        
        for char in s:
            if char not in cur_text:
                cur_text += char
            else:
                target_idx = cur_text.find(char)
                cur_text = cur_text[target_idx + 1:] + char

            if len(cur_text) > longest_str_len:
                longest_str_len = len(cur_text)

        return longest_str_len

            
# @lc code=end

