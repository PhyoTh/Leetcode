from collections import defaultdict, deque
class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for source, target, factor in conversions:
            adj_list[source].append((target, factor))
        
        result = [1 for _ in range(len(conversions) + 1)]
        que = deque([0])
        while que:
            for _ in range(len(que)):
                node = que.popleft()
                if node not in adj_list:
                    continue

                for neighbor, factor in adj_list[node]:
                    result[neighbor] = (result[node] * factor) % (10 ** 9 + 7)
                    que.append(neighbor)
                
        return result