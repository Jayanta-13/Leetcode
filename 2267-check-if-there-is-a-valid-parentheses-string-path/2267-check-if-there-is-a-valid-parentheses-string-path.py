class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        # A valid parentheses string must have even length
        if (m + n - 1) % 2 != 0:
            return False

        # dp[j] = set of possible balances at cell (i, j)
        dp = [set() for _ in range(n)]

        for i in range(m):
            for j in range(n):
                # Starting cell
                if i == 0 and j == 0:
                    if grid[i][j] == ')':
                        return False
                    dp[j].add(1)
                    continue

                # Possible balances from top and left
                possible = set()

                if i > 0:
                    possible.update(dp[j])

                if j > 0:
                    possible.update(dp[j - 1])

                # Calculate new balances
                current = grid[i][j]
                new_balances = set()

                for balance in possible:
                    if current == '(':
                        new_balance = balance + 1
                    else:
                        new_balance = balance - 1

                    # Balance can never be negative
                    if new_balance >= 0:
                        new_balances.add(new_balance)

                dp[j] = new_balances

        return 0 in dp[n - 1]
        