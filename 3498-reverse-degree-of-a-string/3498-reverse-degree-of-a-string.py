class Solution:
    def reverseDegree(self, s: str) -> int:
        total_degree = 0
        for idx, char in enumerate(s, start=1):
            # 'a' = 26, 'b' = 25, ..., 'z' = 1
            rev_alpha_pos = 26 - (ord(char) - ord('a'))
            total_degree += rev_alpha_pos * idx
            
        return total_degree


if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    s1 = "abc"
    print(f'Input: s = "{s1}"')
    print(f"Output: {sol.reverseDegree(s1)}")  # Output: 148

    # Example 2
    s2 = "zaza"
    print(f'Input: s = "{s2}"')
    print(f"Output: {sol.reverseDegree(s2)}")  # Output: 160
        
    
    
        
    
    