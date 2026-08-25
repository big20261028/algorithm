#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return self.findMaxDepth(root.left, root.right)

    def findMaxDepth(self, a_node, b_node, depth=1):
        if not a_node and not b_node:
            return depth

        if not a_node:
            return self.findMaxDepth(b_node.left, b_node.right, depth+1)
        elif not b_node:
            return self.findMaxDepth(a_node.left, a_node.right, depth+1)
        else:
            return max(self.findMaxDepth(a_node.left, a_node.right, depth+1), 
                       self.findMaxDepth(b_node.left, b_node.right, depth+1))
        

    
# @lc code=end

