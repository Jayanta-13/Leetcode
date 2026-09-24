class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        def digit_sum(n: int) -> int:
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total

        for i in range(len(nums)):
            if digit_sum(nums[i]) == i:
                return i

        return -1