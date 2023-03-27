#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if (len(s) <= 1) or s == s[::-1]:
            return s
        else:
            max = 1
            pos = 0
            for i in range(1,len(s)):
                if s[i-max-1:i+1] == s[i-max-1:i+1][::-1]:
                    pos = i-max-1
                    max += 2
                    continue
                if s[i-max:i+1] == s[i-max:i+1][::-1]:
                    pos = i-max
                    max += 1
            return s[pos:pos+max]
                
                










# @lc code=end