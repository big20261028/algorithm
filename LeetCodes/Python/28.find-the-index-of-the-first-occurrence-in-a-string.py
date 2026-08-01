#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        lps = self.build_lps(needle)

        i = 0
        j = 0

        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1

                if j == len(needle):
                    return i - j
            else:
                if j > 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return -1

        # return haystack.find(needle)

    def build_lps(self, pattern: str) -> list[int]:
        lps = [0] * len(pattern)

        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1

            else:
                if length > 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
        
# @lc code=end

