class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        in_deg = [0 for _ in range(numCourses)]
        for course, preq in prerequisites:
            adj_list[preq].append(course)
            in_deg[course] += 1
        
        que = deque()
        for i in range(numCourses):
            if in_deg[i] == 0:
                que.append(i)
        
        visited = []
        while que:
            preq = que.popleft()
            visited.append(preq)
            for course in adj_list[preq]:
                in_deg[course] -= 1

                if in_deg[course] > 0:
                    continue
                
                que.append(course)

        return visited if len(visited) == numCourses else []