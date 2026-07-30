#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        start_node = ListNode(-1)
        result = start_node

        while list1 and list2:
            if list1.val <= list2.val:
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next

            result = result.next

        result.next = list1 or list2

        return start_node.next
        
# @lc code=end

``