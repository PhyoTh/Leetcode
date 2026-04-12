1class Solution:
2    '''
3    classes: [[1,0], [2, 1], [3, 2], [3, 1]]
4
5    adj_list
6    0 > 1
7    1 > 2, 3
8    2 > 3
9    ans: 0 > 1 > 2 > 3
10
11    # notes
12    need to pre process the whole prereq list
13    traverse DAG
14    '''
15    from collections import defaultdict, deque
16    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
17        n = len(prerequisites)
18        if n == 0 or n == 1:
19            return True
20
21        adj_list = defaultdict(list)
22        in_deg = [0 for _ in range(numCourses)]
23
24        for course, prereq in prerequisites:
25            adj_list[prereq].append(course)
26            in_deg[course] += 1
27
28        que = deque(i for i in range(numCourses) if in_deg[i] == 0)
29        visited = 0
30        while que:
31            node = que.popleft()
32            visited += 1
33
34            for neighbor in adj_list[node]:
35                in_deg[neighbor] -= 1
36                if in_deg[neighbor] == 0:
37                    que.append(neighbor)
38
39        return visited == numCourses