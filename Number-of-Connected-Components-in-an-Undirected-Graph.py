class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)
        
        def dfs(x, visited):
            stack = [x]

            while stack:
                node = stack.pop()
                
                for neighbor in adj_list[node]:
                    if neighbor in visited:
                        continue
                    stack.append(neighbor)
                    visited.add(neighbor)

        counter = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i, visited)
                counter += 1

        return counter