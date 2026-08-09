#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        # print(2 ** 31)
        # print(2 ** 32)

        limit_int = 2 ** 31
        # print(test_int)
        result = list(str(x))
        result.reverse()
        last_char = result.pop()
        if last_char == '-':
            result = int("".join(result)) * -1
        else:
            result.append(last_char)
            result = int("".join(result))

        if result >= limit_int or result < limit_int * -1:
            return 0
        
        return result
        
# @lc code=end

