class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        unvisited = set()
        for i in range(n):
            unvisited.add(i)
        
        component = 0
        while unvisited:
            component += 1
            first = next(iter(unvisited))
            stack = [first]
            unvisited.remove(first)
            while stack:
                node = stack.pop()

                for neighbor in adj_list[node]:
                    if neighbor not in unvisited:
                        continue
                    
                    stack.append(neighbor)
                    unvisited.remove(neighbor)
        
        return component