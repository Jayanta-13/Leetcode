class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        # Numbers ending in 0 cannot be palindromes
        # unless the number itself is 0
        if x % 10 == 0 and x != 0:
            return False

        reversed_half = 0

        # Reverse only half of x
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # Even number of digits OR odd number of digits
        return x == reversed_half or x == reversed_half // 10
        