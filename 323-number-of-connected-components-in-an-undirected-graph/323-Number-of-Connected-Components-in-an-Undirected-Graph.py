class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]

        def find(node: int) -> int:
            root = node
            while parents[root] != root:
                root = parents[root]
            while parents[node] != root:
                node, parents[node] = parents[node], root
            return root
        
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
    