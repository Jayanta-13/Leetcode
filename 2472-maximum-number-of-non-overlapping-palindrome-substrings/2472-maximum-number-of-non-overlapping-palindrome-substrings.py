class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            
            # Check for palindrome of length k ending at i - 1
            if i >= k and is_palindrome(s[i - k : i]):
                dp[i] = max(dp[i], dp[i - k] + 1)
            
            # Check for palindrome of length k + 1 ending at i - 1
            if i >= k + 1 and is_palindrome(s[i - k - 1 : i]):
                dp[i] = max(dp[i], dp[i - k - 1] + 1)
                
        return dp[n]
        