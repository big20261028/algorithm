#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:

        '''
        1. 공백은 무시
        2. + or - 나오면 반영. 단, 숫자가 나오지 않은 상태일때만,
        3. 숫자가 없으면 0 반환
        4. -2의 31제곱보다 작으면 -2의 31제곱 값을 쓰고 2의 31제곱-1 보다 크면 2의 31제곱-1 값 반환

        '''
        # 공백을 모두 제거함
        # s = s.replace(" ","")
        result = None

        is_minus = None
        max_val = (2 ** 31) - 1
        min_val = (-2) ** 31

        char_number_list = list()

        '''
        char가 숫자이면 append
        리스트가 차있고 char_number_list[0] 가 0이면 덮어쓰기

        '''
        # print(s)
        for char in s:


            if not char_number_list and is_minus is None and char == "-":
                is_minus = True
            elif not char_number_list and is_minus is None and char == "+":
                is_minus = False
            elif is_minus is not None and not char.isdecimal():
                break
            elif char == " ":
                print(char)
                if char_number_list:
                    break
                else:
                    continue

            elif not char.isdecimal():
                print(char)
                break
            else:
                if char_number_list and char_number_list[0] == '0':
                    char_number_list[0] = char
                else:
                    print(char)
                    char_number_list.append(char)



        if char_number_list:
            result = int("".join(char_number_list))
            if is_minus:
                result *= -1

        if result:
            if result > max_val:
                return max_val
            elif result < min_val:
                return min_val
            else:
                return result
        else:
            return 0



        
# @lc code=end

