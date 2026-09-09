#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        시작포인터 0, 끝포인터 len(height) - 1
        시작포인터와 끝포인터 사이의 넓이 구하기
        시작포인터 + 1 하여 다시 넓이 구하기
        +1 값이 더하기 전 넓이보다 크면 포인터 이동시키고 작거나 같으면 유지

        유지가 될 경우 끝포인터 앞으로 이동
        -----폐기-----
        끝포인터 고정 후 시작포인터 뒤로 옮겨가며 최대 넓이 구하기
        최대 넓이를 갱신하면 포인터 옮기고 작거나 같으면 pass
        이후 끝포인터 이동 후, 넓이 계산하여 넓이가 크면 이전 공정 실행 작거나 같으면 무시(같을경우 고민해볼 필요 있음)
        반복하며 최대값 갱신하고 두 포인터가 만나면 종료 

        '''
        start_pointer = 0
        end_pointer = len(height) - 1

        max_store = float('-inf')

        while end_pointer > start_pointer:
            current_x = end_pointer - start_pointer
            current_y = min(height[end_pointer], height[start_pointer])
            current_space = current_x * current_y

            if current_space > max_store:
                max_store = current_space

                for next_idx in range(start_pointer + 1, end_pointer):
                    next_x = end_pointer - next_idx
                    next_y = min(height[end_pointer], height[next_idx])
                    next_space = next_x * next_y

                    if next_space > max_store:
                        max_store = next_space
                        current_x = next_x
                        current_y = next_y
                        start_pointer = next_idx
                    elif next_space == max_store and ((next_x - current_x) < (next_y - current_y)):
                        current_x = next_x
                        current_y = next_y
                        start_pointer = next_idx



            


        
# @lc code=end

