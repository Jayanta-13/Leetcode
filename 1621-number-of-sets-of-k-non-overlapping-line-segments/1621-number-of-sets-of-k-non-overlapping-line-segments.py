class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # We need to calculate C(n + k - 1, 2 * k) % MOD
        N = n + k - 1
        R = 2 * k
        
        if R > N:
            return 0
        
        # Calculate combination using modular inverse
        num = 1
        den = 1
        for i in range(1, R + 1):
            num = (num * (N - i + 1)) % MOD
            den = (den * i) % MOD
            
        return (num * pow(den, MOD - 2, MOD)) % MOD
        