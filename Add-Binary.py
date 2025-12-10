1class Solution:
2    def three_bit_addition(self, bit_a, bit_b, bit_c):
3        bit_a, bit_b, bit_c = int(bit_a), int(bit_b), int(bit_c)
4        total = bit_a + bit_b + bit_c  # 0, 1, 2, or 3
5
6        result_bit = str(total % 2)
7        carry_bit = str(total // 2)
8        return result_bit, carry_bit
9
10    def addBinary(self, a: str, b: str) -> str:
11        walker_a = len(a) - 1
12        walker_b = len(b) - 1
13
14        result = ""
15        carry_bit = '0'
16        while walker_a >= 0 or walker_b >= 0:
17            char_a = a[walker_a] if walker_a >= 0 else '0'
18            char_b = b[walker_b] if walker_b >= 0 else '0'
19
20            result_bit, carry_bit = self.three_bit_addition(char_a, char_b, carry_bit)
21            result += result_bit
22
23            walker_a -= 1
24            walker_b -= 1
25
26        if carry_bit == '1':
27            result += carry_bit
28        return result[::-1]
29