#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result_list = list()
        
        while columnNumber:
            columnNumber -= 1
            left_val = columnNumber % 26
            # if not left_val:
            #     left_val = 26
            # left_val -= 1
            target_char = chr(65 + left_val)
            result_list.append(target_char)


            columnNumber //= 26
        result_list.reverse()
        return "".join(result_list)




        
# @lc code=end

