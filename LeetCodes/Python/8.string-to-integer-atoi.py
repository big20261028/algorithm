#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:

        flag = True
        result = list()

        is_positive = True
        limit_range = 2 ** 31

        for char in s:

            if char == ' ' and flag:
                continue

            if char == '-' and flag:
                is_positive = False
            elif char == '+' and flag:
                pass
            
            elif not result and char == '0':
                pass

            elif char.isdigit():
                result.append(char)
            else:
                break

            flag = False

        if not result:
            return 0

        if is_positive:
            result = int("".join(result))
        else:
            result = int("".join(result)) * -1

        if result >= limit_range:
            result = limit_range - 1
        elif result < (limit_range * -1):
            result = (limit_range * -1)

        return result

        
# @lc code=end

