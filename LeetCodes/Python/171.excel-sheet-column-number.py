#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        position_idx = 0
        result = 0

        char_list = list(columnTitle)

        while char_list:
            target_char = char_list.pop()
            target_val = (ord(target_char) - 64) * (26 ** position_idx)
            result += target_val
            position_idx += 1

        return result

        
# @lc code=end

