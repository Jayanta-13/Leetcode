class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')
        
        # min_len[i] stores the min length of a valid subarray ending at or before index i
        min_len = [INF] * n
        
        left = 0
        current_sum = 0
        min_total_length = INF
        current_min = INF
        
        for right in range(n):
            current_sum += arr[right]
            
            # Shrink window from the left if sum exceeds target
            while current_sum > target and left <= right:
                current_sum -= arr[left]
                left += 1
                
            # Found a valid subarray with sum equal to target
            if current_sum == target:
                length = right - left + 1
                
                # Check if a non-overlapping valid subarray exists before 'left'
                if left > 0 and min_len[left - 1] != INF:
                    min_total_length = min(min_total_length, min_len[left - 1] + length)
                
                # Update the minimum subarray length seen so far up to index 'right'
                current_min = min(current_min, length)
                
            min_len[right] = current_min
            
        return min_total_length if min_total_length != INF else -1