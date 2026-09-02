#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        prev = 1

        for r in range(1, rowIndex + 1):
            next_val = prev * (rowIndex - r + 1) // r
            result.append(next_val)
            prev = next_val

        return result

# @lc code=end

