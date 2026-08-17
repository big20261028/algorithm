#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first_node = ListNode()
        second_node = first_node
        used_num = set()

        while head:
            if head.val in used_num:
                head = head.next
                continue

            used_num.add(head.val)
            second_node.next = head

            second_node = second_node.next
            head = head.next
            second_node.next = None

        return first_node.next
        
        
        
# @lc code=end

