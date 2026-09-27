class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == ')':
                # Pop characters until we hit the matching '('
                curr = []
                while stack and stack[-1] != '(':
                    curr.append(stack.pop())
                
                # Pop the opening '('
                stack.pop()
                
                # Push the reversed characters back onto the stack
                stack.extend(curr)
            else:
                stack.append(char)
                
        return "".join(stack)
        