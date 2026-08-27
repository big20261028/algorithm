#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # val_list = list()
        # self.makeList(nums, val_list)
        new_tree = TreeNode()
        self.makeNewTree(new_tree, nums)
        return new_tree

    # def makeList(self, node, temp_list):
    #     if not node:
    #         return

    #     temp_list.append(node.val)

    #     if not node.left:
    #         self.makeList(node.left, temp_list)

    #     if not node.right:
    #         self.makeList(node.right, temp_list)

    def makeNewTree(self, node, temp_list):
        if not temp_list:
            node.val = None
            return

        center_idx = len(temp_list) // 2

        node.val = temp_list[center_idx]

        if temp_list[:center_idx]:
            node.left = TreeNode()
            self.makeNewTree(node.left, temp_list[:center_idx])

        if temp_list[center_idx + 1:]:
            node.right = TreeNode()
            self.makeNewTree(node.right, temp_list[center_idx + 1:])
        # node.right = temp_list[center_idx + 1:]

        
# @lc code=end

