1class Solution:
2    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
3        adj_list = defaultdict(list)
4        in_deg = [0 for _ in range(numCourses)]
5
6        for course, prereq in prerequisites:
7            adj_list[prereq].append(course)
8            in_deg[course] += 1
9
10        que = deque(i for i in range(numCourses) if in_deg[i] == 0)
11        result = []
12        while que:
13            node = que.popleft()
14            result.append(node)
15
16            for neighbor in adj_list[node]:
17                in_deg[neighbor] -= 1
18                if in_deg[neighbor] == 0:
19                    que.append(neighbor)
20
21        if len(result) != numCourses:
22            return []
23
24        return result