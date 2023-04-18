# 3. Longest Substring Without Repeating Characters
'''
Given a string s, find the length of the longest
substring
 without repeating characters.
 '''
'''example:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''

class Solution:
    def __init__(self, name):
        self.input = name
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        left_cursor = 0
        used = {}

        for right_cursor, char in enumerate(s):
            if char in used and left_cursor <= used[char]:  # Duplicated character
                left_cursor = used[char] + 1
            else:
                ans = max(ans, right_cursor - left_cursor + 1)
            used[char] = right_cursor

        return ans


# https://leetcode.com/problems/longest-palindromic-substring/
# class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        i,l=0,0
        for j in range(len(s)):
            if s[j-l: j+1] == s[j-l: j+1][::-1]:
                i, l = j-l, l+1
                # print(s[i: i+l])
            elif j-l > 0 and s[j-l-1: j+1] == s[j-l-1: j+1][::-1]:
                i, l = j-l-1, l+2
                # print(s[i: i+l])
        return s[i: i+l]






# if __name__ == '__main__':
#     sol = Solution("babdd")
#     sol.longestPalindrome("babdd")


