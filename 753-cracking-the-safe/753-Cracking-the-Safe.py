class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        visited = set()
        result = []

        def dfs(node: str):
            for i in range(k):
                new_node = node + str(i)

                if new_node in visited:
                    continue
                
                visited.add(new_node)
                dfs(new_node[1:])
                result.append(str(i))

        start_node = '0' * (n - 1)
        dfs(start_node)
        return ''.join(result) + start_node