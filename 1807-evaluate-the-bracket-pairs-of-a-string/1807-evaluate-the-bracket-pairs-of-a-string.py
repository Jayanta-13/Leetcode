class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Convert knowledge array to a hash map for O(1) key lookups
        lookup = {key: value for key, value in knowledge}
        
        res = []
        in_bracket = False
        current_key = []
        
        for char in s:
            if char == '(':
                in_bracket = True
            elif char == ')':
                in_bracket = False
                key_str = "".join(current_key)
                res.append(lookup.get(key_str, "?"))
                current_key = []
            else:
                if in_bracket:
                    current_key.append(char)
                else:
                    res.append(char)
                    
        return "".join(res)
        