#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        new_node_head = ListNode()
        new_node_current = new_node_head
        
        while head:
            while head and head.val == val:
                head = head.next
            new_node_current.next = head
            new_node_current = new_node_current.next
            head = head.next if head else None
            
        return new_node_head.next
        
        
        
# @lc code=end

