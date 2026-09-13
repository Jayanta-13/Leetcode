from collections import defaultdict
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        # Store coordinates of all 1s in img1 and img2
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        # Map translation vectors (dr, dc) to their count of overlapping 1s
        overlap_counts = defaultdict(int)
        
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                # Vector required to shift the 1 in img1 to line up with the 1 in img2
                dr = r2 - r1
                dc = c2 - c1
                overlap_counts[(dr, dc)] += 1
                
        # Return maximum overlaps achieved by any single translation vector
        return max(overlap_counts.values()) if overlap_counts else 0
        