class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(expr: str) -> set[str]:
            # Base case: single character
            if len(expr) == 1:
                return {expr}
            
            # Step 1: Split by top-level commas (Unions)
            groups = []
            level = 0
            current_group = []
            
            for char in expr:
                if char == '{':
                    level += 1
                    current_group.append(char)
                elif char == '}':
                    level -= 1
                    current_group.append(char)
                elif char == ',' and level == 0:
                    groups.append("".join(current_group))
                    current_group = []
                else:
                    current_group.append(char)
            groups.append("".join(current_group))
            
            # If we had top-level commas, calculate the union of all groups
            if len(groups) > 1:
                res = set()
                for group in groups:
                    res |= parse(group)
                return res
            
            # Step 2: Peel outermost braces if the whole expression is enclosed by them
            if expr.startswith('{') and expr.endswith('}'):
                level = 0
                is_surrounded = True
                for i, char in enumerate(expr):
                    if char == '{':
                        level += 1
                    elif char == '}':
                        level -= 1
                    if level == 0 and i < len(expr) - 1:
                        is_surrounded = False
                        break
                if is_surrounded:
                    return parse(expr[1:-1])
            
            # Step 3: Handle Concatenations
            concat_blocks = []
            i = 0
            while i < len(expr):
                if expr[i] == '{':
                    start = i
                    level = 1
                    i += 1
                    while i < len(expr) and level > 0:
                        if expr[i] == '{':
                            level += 1
                        elif expr[i] == '}':
                            level -= 1
                        i += 1
                    concat_blocks.append(parse(expr[start:i]))
                else:
                    concat_blocks.append({expr[i]})
                    i += 1
            
            # Compute Cartesian product across all concatenation blocks
            res = set()
            for prod in itertools.product(*concat_blocks):
                res.add("".join(prod))
                
            return res

        return sorted(list(parse(expression)))