class Solution:
    def __init__(self):
        self.parents = {}
    
    def find(self, node: int) -> int:
        x = node
        while self.parents[x] != x:
            x = self.parents[x]
        
        self.parents[node] = x
        return x
    
    def union(self, a: int, b: int) -> bool:
        a_parent, b_parent = self.find(a), self.find(b)

        if a_parent == b_parent:
            return False
        elif a_parent < b_parent:
            self.parents[b_parent] = a_parent
        else:
            self.parents[a_parent] = b_parent
        return True
        
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        last = [-1, -1]

        for a, b in edges:
            if a not in self.parents:
                self.parents[a] = a
            if b not in self.parents:
                self.parents[b] = b
            
            if not self.union(a, b):
                last = [a, b]
        
        return last
    
    '''
    parents = {
        1: 1
        2: 1
        3: 1
        4: 1
    }
    a, b = 4, 1
    a_parent, b_parent = 1, 1
    '''