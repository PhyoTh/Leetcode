class Node():
    def __init__(self, var):
        self.var = var

class Solution(object):
    def __init__(self):
        self.seen = set() # store strings
        self.edges = {} # ("var1", "var2"): edge_value

    def make_graph(self, equations, values):
        for i, [var1, var2] in enumerate(equations):
            # assuming that there is no duplicate
            self.edges[(var1, var2)] = values[i]
            self.edges[(var2, var1)] = 1 / values[i]
            self.seen.add(var1)
            self.seen.add(var2)
    
    def dfs(self, s_node, t_node):
        if s_node == t_node:
            return 1.0

        visited = set([s_node])
        explore = [(s_node, 1.0)] # (node, accumulate edge value)
        
        while len(explore) != 0:
            current_node, current_value = explore.pop() # pop the last-in node

            for (node1, node2), edge_value in self.edges.items():
                if node1 == current_node and node2 not in visited:
                    if node2 == t_node:
                        return current_value * edge_value
                    explore.append((node2, current_value * edge_value))
                    visited.add(node2)
    
        return -1.0

    def calcEquation(self, equations, values, queries):
        self.make_graph(equations, values)

        result = []
        for [s_node, t_node] in queries:
            if s_node not in self.seen or t_node not in self.seen:
                result.append(-1.0)
                continue
            
            if (s_node, t_node) in self.edges:
                result.append(self.edges[(s_node, t_node)])
                continue
            elif (t_node, s_node) in self.edges:
                result.append(self.edges[(t_node, s_node)])
                continue

            value = self.dfs(s_node, t_node)
            result.append(value)

        return result