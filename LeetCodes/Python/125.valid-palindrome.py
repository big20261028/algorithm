#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s.isdecimal()
        # s.isalpha()
        # print(s.lower())
        s = s.lower()
        temp_list = list()

        for char in s:
            if char.isalpha() or char.isdecimal():
                temp_list.append(char)

        # print(temp_list)
        s = "".join(temp_list)
        # print(s)

        str_len = len(s)

        front_pointer = 0
        back_pointer = str_len - 1

        while front_pointer <= back_pointer:

            while not (s[front_pointer].isalpha() or s[front_pointer].isdecimal()):
                # print(s[front_pointer], s[front_pointer].isalpha(), s[front_pointer].isdecimal())
                if front_pointer + 1 > back_pointer:
                    return False
                else:
                    front_pointer += 1

            while not (s[back_pointer].isalpha() or s[back_pointer].isdecimal()):
                # print(s[back_pointer], s[back_pointer].isalpha(), s[back_pointer].isdecimal())
                if back_pointer - 1 < front_pointer:
                    return False
                else:
                    back_pointer -= 1

            # print(s[front_pointer], s[back_pointer])
            if s[front_pointer] != s[back_pointer]:
                return False
            else:
                front_pointer += 1
                back_pointer -= 1

        return True

        
# @lc code=end

