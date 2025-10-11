class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict, deque
        indegree = [0] * numCourses  # indegree[i] = number of incoming edges to i node
        edge_map = defaultdict(set)  # prereq : set(courses)

        for course, prereq in prerequisites:
            edge_map[prereq].add(course)
            indegree[course] += 1

        explore = deque([])
        for course, num_indegree in enumerate(indegree):
            if num_indegree == 0:
                explore.append(course)

        nodesVisited = 0
        while explore:
            prereq = explore.popleft()
            for course in edge_map[prereq]:
                # remove edge
                indegree[course] -= 1
                # add to explore
                if indegree[course] == 0:
                    explore.append(course)
            nodesVisited += 1

        return True if nodesVisited == numCourses else False
