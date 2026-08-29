from collections import defaultdict, deque


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipes_set = set(recipes)
        adj_list = defaultdict(list)
        in_deg = defaultdict(int)
        for i, recipe in enumerate(recipes): # O(n)
            for ingredient in ingredients[i]: # O(m)
                adj_list[ingredient].append(recipe)
                in_deg[recipe] += 1

        que = deque(supplies)
        
        result = []
        while que:
            node = que.popleft()

            if node in recipes_set:
                result.append(node)

            for neighbor in adj_list[node]:
                in_deg[neighbor] -= 1
                if in_deg[neighbor] == 0:
                    que.append(neighbor)

        return result
