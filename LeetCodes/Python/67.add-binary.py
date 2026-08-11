#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        target_idx = 0
        a_list = list(a)
        b_list = list(b)

        result = list()
        flag = False
        while a_list and b_list:
            target_val = 1 if flag else 0
            a_char = a_list.pop()
            if a_char == "1":
                target_val += 1
            b_char = b_list.pop()
            if b_char == "1":
                target_val += 1

            flag = target_val >= 2

            result.append(str(target_val % 2))

            target_idx += 1

        while a_list:
            target_val = 1 if flag else 0
            if a_list.pop() == "1":
                target_val += 1
            flag = target_val >= 2
            result.append(str(target_val % 2))

        while b_list:
            target_val = 1 if flag else 0
            if b_list.pop() == "1":
                target_val += 1
            flag = target_val >= 2
            result.append(str(target_val % 2))

        if flag:
            result.append("1")

        return "".join(result[::-1])

        
# @lc code=end

