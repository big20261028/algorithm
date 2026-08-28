#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = self.getHeight(root)
        if result != -1:
            return True
        else:
            return False

    def getHeight(self, node: Optional[TreeNode]):
        if not node:
            return 0

        left_height = self.getHeight(node.left)
        right_height = self.getHeight(node.right)

        if left_height != -1 and right_height != -1 and (abs(left_height - right_height) <= 1):
            return 1 + max(left_height, right_height)
        else:
            return -1
# @lc code=end

