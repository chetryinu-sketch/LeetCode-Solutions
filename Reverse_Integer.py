"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 
Constraints:

-231 <= x <= 231 - 1
"""
def sign(num):
    return -1 if num<0 else 1

class Solution:
    def reverse(self, x: int) -> int:
        s=sign(x)
        x=x*s

        rev=0
        while x!=0:
            last_digit = x % 10
            rev = rev * 10 + last_digit
            x //= 10
        return rev*s
    
q=Solution()
print(q.reverse(-123450))


# x = 12345; rev = 0
# x = 1234; rev = 5
# x = 123; rev = 54
# x = 12; rev = 543
# x = 1; rev = 5432
# x = 0; rev = 54321 <-

        