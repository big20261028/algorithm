#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        # visited.add(head)
        # print(head in visited)
        while head:
            # print(head.val)
            if head in visited:
                return True
            else:
                visited.add(head)
            head = head.next
        return False

        
# @lc code=end

