#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list = s.split()
        target_word = word_list.pop()
        return len(target_word)
        
# @lc code=end

