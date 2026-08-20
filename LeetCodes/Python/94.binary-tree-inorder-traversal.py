#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder_search(self, node, result):
        if node.left:
            self.inorder_search(node.left, result)
        result.append(node.val)
        if node.right:
            self.inorder_search(node.right, result)

        

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # print(root)
        # print(root.val)
        # print(root.left)
        # print(root.right)

        result = list() 
        if root:
            self.inorder_search(root, result)
        return result
        
# @lc code=end

