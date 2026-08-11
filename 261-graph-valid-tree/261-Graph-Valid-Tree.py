class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False
        
        parent = [i for i in range(n)]

        def find(node: int):
            parent_node = parent[node]
            while parent_node != node:
                node = parent_node
                parent_node = parent[node]
            return parent_node
        
        def union(a: int, b: int) -> bool:
            a_parent = find(a)
            b_parent = find(b)
            if a_parent == b_parent:
                return False
            
            if a_parent < b_parent:
                parent[b_parent] = a_parent
            else:
                parent[a_parent] = b_parent
            return True
        
        for a, b in edges:
            if not union(a, b):
                return False
        
        return True