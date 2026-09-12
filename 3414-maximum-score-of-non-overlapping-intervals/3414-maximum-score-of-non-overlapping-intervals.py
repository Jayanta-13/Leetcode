from bisect import bisect_left
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
        # Store intervals with original indices: (l, r, weight, original_index)
        sorted_intervals = sorted(
            [(intervals[i][0], intervals[i][1], intervals[i][2], i) for i in range(n)],
            key=lambda x: x[1]  # Sort by right endpoint r
        )
        
        # Extract right endpoints for binary search
        r_ends = [interval[1] for interval in sorted_intervals]
        
        # dp[i][k] stores (max_weight, tuple_of_indices) using at most k intervals from first i intervals
        dp = [[(0, ())] * 5 for _ in range(n + 1)]

        for i in range(1, n + 1):
            l, r, w, idx = sorted_intervals[i - 1]
            
            # Find the latest interval ending strictly before current start `l`
            prev_idx = bisect_left(r_ends, l)
            
            for k in range(1, 5):
                # Option 1: Exclude current interval
                best_without = dp[i - 1][k]
                
                # Option 2: Include current interval
                prev_weight, prev_indices = dp[prev_idx][k - 1]
                new_weight = prev_weight + w
                new_indices = tuple(sorted(prev_indices + (idx,)))
                best_with = (new_weight, new_indices)
                
                # Compare options: max weight first, then lexicographically smaller indices
                if best_with[0] > best_without[0]:
                    dp[i][k] = best_with
                elif best_with[0] < best_without[0]:
                    dp[i][k] = best_without
                else:
                    dp[i][k] = best_with if best_with[1] < best_without[1] else best_without

        # Find the overall best result across choice count 1 to 4
        best_weight = 0
        best_indices = ()
        
        for k in range(1, 5):
            w, indices = dp[n][k]
            if w > best_weight:
                best_weight = w
                best_indices = indices
            elif w == best_weight and w > 0:
                if indices < best_indices:
                    best_indices = indices
                    
        return list(best_indices)