#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows >= len(s):
            return s

        result = []
        cycle = 2 * (numRows - 1)

        for r in range(numRows):
            step1 = cycle - 2 * r
            step2 = 2 * r
            
            idx = r
            flag = True

            while idx < len(s):
                result.append(s[idx])

                if step2 == 0:
                    idx += step1
                elif step1 == 0:
                    idx += step2
                else:
                    idx += step1 if flag else step2
                    flag = not flag

        return "".join(result)

        
# @lc code=end

