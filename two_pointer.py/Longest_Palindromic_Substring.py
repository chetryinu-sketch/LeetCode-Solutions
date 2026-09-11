"""
Given a string s, return the longest palindromic substring in s.
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 
Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        i=0
        j=len(s)-1
        sub_str=""
        while i<j:
            if s[i]==s[j]:
                sub_str = s[i:j+1]
            i+=1
            j-=1
        return sub_str

obj=Solution()
print(obj.longestPalindrome("cbbd"))

                


                