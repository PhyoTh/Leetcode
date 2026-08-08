class Solution:
    '''
    classes: [[1,0], [2, 1], [3, 2], [3, 1]]

    adj_list
    0 > 1
    1 > 2, 3
    2 > 3
    ans: 0 > 1 > 2 > 3

    # notes
    need to pre process the whole prereq list
    traverse DAG
    '''
    from collections import defaultdict, deque
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = len(prerequisites)
        if n == 0 or n == 1:
            return True

        adj_list = defaultdict(list)
        in_deg = [0 for _ in range(numCourses)]

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            in_deg[course] += 1

        que = deque(i for i in range(numCourses) if in_deg[i] == 0)
        visited = 0
        while que:
            node = que.popleft()
            visited += 1

            for neighbor in adj_list[node]:
                in_deg[neighbor] -= 1
                if in_deg[neighbor] == 0:
                    que.append(neighbor)

        return visited == numCourses