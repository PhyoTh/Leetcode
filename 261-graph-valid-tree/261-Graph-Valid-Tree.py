class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False
        
        adj_list = [[] for _ in range(n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        stack = [0]
        visited = set([0])

        while stack:
            node = stack.pop()

            for neighbor in adj_list[node]:
                if neighbor in visited:
                    continue
                
                stack.append(neighbor)
                visited.add(neighbor)
            
        return len(visited) == n