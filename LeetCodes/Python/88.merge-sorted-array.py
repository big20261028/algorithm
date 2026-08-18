#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        copy_list = list()

        nums1_idx = 0
        nums2_idx = 0

        while nums1_idx < m and nums2_idx < n:
            nums1_val = nums1[nums1_idx]
            nums2_val = nums2[nums2_idx]

            if nums1_val <= nums2_val:
                copy_list.append(nums1_val)
                nums1_idx += 1
            else:
                copy_list.append(nums2_val)
                nums2_idx += 1   

        copy_list = copy_list + nums1[nums1_idx:m] + nums2[nums2_idx:n]
        # print(copy_list)
        # nums1 = copy_list

        for idx, val in enumerate(nums1):
            nums1[idx] = copy_list[idx]

            

        # copy_list[0] = 100
        # print(copy_list, nums1)
        
# @lc code=end

