1from collections import defaultdict
2class Solution:
3    def __init__(self):
4        self.parent = {}
5        self.rank = defaultdict(int) # sets rank to 0 by default
6
7    def find(self, node):
8        if self.parent[node] == node:
9            return node
10        return self.find(self.parent[node])
11        
12    def union(self, u, v):
13        u_parent = self.find(u)
14        v_parent = self.find(v)
15
16        if self.rank[u_parent] > self.rank[v_parent]:
17            self.parent[v_parent] = u_parent
18        elif self.rank[u_parent] < self.rank[v_parent]:
19            self.parent[u_parent] = v_parent
20        else:
21            self.parent[v_parent] = u_parent
22            self.rank[u_parent] += 1 # only increment when both ranks have same height
23
24    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
25        for [u, v] in edges:
26            # init the parents for new nodes
27            if u not in self.parent:
28                self.parent[u] = u
29            if v not in self.parent:
30                self.parent[v] = v
31            
32            if self.find(u) == self.find(v): # cycle!
33                return [u, v]
34
35            self.union(u, v)
36