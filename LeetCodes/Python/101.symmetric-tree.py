#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.mirrorTreeCheck(root.left, root.right)


    def mirrorTreeCheck(self, a_root: Optional[TreeNode], b_root: Optional[TreeNode]):

        if not a_root and not b_root:
            return True

        if not a_root or not b_root or a_root.val != b_root.val:
            return False

        return self.mirrorTreeCheck(a_root.left, b_root.right) and self.mirrorTreeCheck(a_root.right, b_root.left)

        # if not self.flag:
        #     return False

        # if not a_root or not b_root:
        #     self.flag = False
        # elif a_root.val != b_root.val:
        #     self.flag = False
        # else:
        #     if not a_root.left and not b_root.right:
        #         pass
        #     elif not a_root.left or not b_root.right:
        #         self.mirrorTreeCheck(a_root.left, b_root.right)


        #     if not a_root.right and not b_root.left:
        #         pass
        #     elif not a_root.right or not b_root.left:
        #         self.mirrorTreeCheck(a_root.right, b_root.left)

        # return self.flag



        


        
# @lc code=end

