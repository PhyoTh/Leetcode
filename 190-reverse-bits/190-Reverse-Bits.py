class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            bit = n & 1
            n >>= 1
            res = (res << 1) | bit
        return res