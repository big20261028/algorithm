#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        start_node = ListNode()
        result = start_node
        flag = False

        while l1 or l2:
            result.next = ListNode()
            result = result.next
            # print(l1)
            # print(l2)

            if l1:
                one_num = l1.val
                l1 = l1.next
            else:
                one_num = 0

            if l2:
                two_num = l2.val
                l2 = l2.next
            else:
                two_num = 0

            sum_num = one_num + two_num
            if flag: 
                sum_num += 1
                flag = False

            if sum_num // 10:
                flag = True

            result.val = sum_num % 10

            # print(l1,l2)

        if flag:
            result.next = ListNode(val=1)            

        return start_node.next

        
# @lc code=end

