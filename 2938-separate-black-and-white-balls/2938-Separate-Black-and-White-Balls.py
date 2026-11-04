class Solution:
    def minimumSteps(self, s: str) -> int:
        inversion_count = 0
        total = 0
        for color in s:
            if color == '1':
                inversion_count += 1
            else:
                total += inversion_count
        return total