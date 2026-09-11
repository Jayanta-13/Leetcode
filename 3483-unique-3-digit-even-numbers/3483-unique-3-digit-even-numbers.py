class Solution:
    def totalNumbers(self, digits):
        count = 0

        # Frequency of each digit in the input
        freq = [0] * 10
        for d in digits:
            freq[d] += 1

        # Try every 3-digit number
        for num in range(100, 1000, 2):
            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            # Count digits needed for this number
            need = [0] * 10
            need[a] += 1
            need[b] += 1
            need[c] += 1

            # Check whether we have enough copies
            possible = True

            for d in range(10):
                if need[d] > freq[d]:
                    possible = False
                    break

            if possible:
                count += 1

        return count
        