#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [ list() for _ in range(numRows) ]
        result[0].append(1)

        

        for row in range(1, numRows):
            temp_list = list()
            prev_list = result[row - 1]
            # print(result)
            # print(prev_list)
            
            for idx in range(row + 1):
                if idx == 0 or idx == len(prev_list):
                    temp_list.append(1)
                else:
                    val = prev_list[idx - 1] + prev_list[idx]
                    temp_list.append(val)

            result[row] = temp_list

        return result
                
                
        
# @lc code=end

