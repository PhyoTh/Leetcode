class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]

        def find(node: int) -> int:
            parent_node = parents[node]
            while parent_node != node:
                node = parent_node
                parent_node = parents[node]
            return parent_node
        
        def union(a: int, b: int) -> None:
            parent_a = find(a)
            parent_b = find(b)
            if parent_a == parent_b:
                return
            
            if parent_a < parent_b:
                parents[parent_b] = parent_a
            else:
                parents[parent_a] = parent_b
        
        for a, b in edges:
            union(a, b)
        
        unique_roots = set()
        for i in range(n):
            unique_roots.add(find(i))
        return len(unique_roots)
    