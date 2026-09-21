class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        result = [0] * k
        dp = [0] * k  # dp[r]: count of subarrays ending at current index with product % k == r

        for num in nums:
            val = num % k
            next_dp = [0] * k
            
            # Start a new subarray with the current element
            next_dp[val] += 1
            
            # Extend existing subarrays
            for r in range(k):
                if dp[r] > 0:
                    new_r = (r * val) % k
                    next_dp[new_r] += dp[r]
            
            # Accumulate into global result
            for r in range(k):
                result[r] += next_dp[r]
            
            dp = next_dp

        return result
        