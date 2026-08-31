#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.findTarget(root, targetSum, 0)

    def findTarget(self, node, target: int, prefix: int):
        if not node:
            return False
        prefix += node.val

        if not node.left and not node.right:
            return prefix == target

        return self.findTarget(node.left, target, prefix) or self.findTarget(node.right, target, prefix)
        
# @lc code=end

