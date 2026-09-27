from collections import defaultdict, deque
class Solution:
    def alienOrder(self, words: list[str]) -> str:
        all_chars = set()
        adj_list = defaultdict(list)
        in_deg = defaultdict(int)

        for word in words: # O(n)
            all_chars.update(word)
        
        for i in range(len(words) - 1): # O(n)
            p1, p2 = 0, 0
            while p1 < len(words[i]) and p2 < len(words[i + 1]):
                if words[i][p1] != words[i + 1][p2]:
                    adj_list[words[i][p1]].append(words[i + 1][p2])
                    in_deg[words[i + 1][p2]] += 1
                    break
                p1 += 1
                p2 += 1
            
            if (p1 == len(words[i]) or p2 == len(words[i + 1])) and len(words[i]) > len(words[i + 1]):
                return ""
        
        que = deque()
        for char in all_chars:
            if in_deg[char] == 0:
                que.append(char)
        
        visited = set()
        result = []
        while que:
            char = que.popleft()
            visited.add(char)
            result.append(char)

            for nxt in adj_list[char]:
                if nxt in visited:
                    return ""
                
                in_deg[nxt] -= 1
                if in_deg[nxt] == 0:
                    que.append(nxt)
        return  ''.join(result) if len(result) == len(all_chars) else "" 