#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        if root:
            self.preorderSearch(root, result)
        return result

    def preorderSearch(self, node, result_list):
        # print(node, node.val)
        if not node:
            return
        result_list.append(node.val)

        if node.left:
            self.preorderSearch(node.left, result_list)
        if node.right:
            self.preorderSearch(node.right, result_list)
        

        
# @lc code=end

