class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Step 1: Record first and last occurrence for each character
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i
            
        intervals = []
        
        # Step 2: Try building a valid interval starting at the first occurrence of each character
        for ch in first:
            i1 = first[ch]
            i2 = last[ch]
            valid = True
            
            j = i1
            while j <= i2:
                char_j = s[j]
                
                # If a character inside needs to start before i1, 
                # this interval will be handled by that earlier character.
                if first[char_j] < i1:
                    valid = False
                    break
                
                # Expand the right bound if needed
                i2 = max(i2, last[char_j])
                j += 1
                
            if valid:
                intervals.append((i1, i2))
                
        # Step 3: Sort intervals by end index (Greedy Interval Scheduling)
        intervals.sort(key=lambda x: x[1])
        
        res = []
        prev_end = -1
        
        for start, end in intervals:
            if start > prev_end:
                res.append(s[start:end + 1])
                prev_end = end
                
        return res
        