1class Solution:
2    def myAtoi(self, s: str) -> int:
3        stack = []
4        neg = None
5        digit_encounter = False
6        
7        for char in s:
8            # Leading spaces are ONLY okay if we haven't seen a sign or digit yet
9            if char == " " and not digit_encounter and neg is None:
10                continue
11            
12            # A minus sign is ONLY okay if we haven't seen a sign or digit yet
13            elif char == "-" and not digit_encounter and neg is None:
14                neg = True
15                
16            # A plus sign is ONLY okay if we haven't seen a sign or digit yet
17            elif char == "+" and not digit_encounter and neg is None:
18                neg = False
19                
20            # Digits are always processed
21            elif char.isdigit():
22                digit_encounter = True
23                stack.append(int(char))
24                
25            # Any other character AFTER we started parsing instantly breaks the loop
26            else:
27                break
28        
29        result = 0
30        for i, digit in enumerate(stack):
31            result += digit * 10 ** (len(stack) - i - 1)
32            
33        if neg:
34            result *= -1
35            
36        INT_MIN, INT_MAX = -2**31, 2**31 - 1
37        if result < INT_MIN:
38            return INT_MIN
39        if result > INT_MAX:
40            return INT_MAX
41            
42        return result