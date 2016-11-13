# # https://leetcode.com/problems/course-schedule-ii/

# There are a total of n courses you have to take, labeled from 0 to n - 1.

# Some courses may have prerequisites, for example to take course 0 
# you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, 
# return the ordering of courses you should take to finish all courses.

# There may be multiple correct orders, you just need to return one of them. 
# If it is impossible to finish all courses, return an empty array.


# For example:

# 2, [[1,0]]
# There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So the correct course order is [0,1]

# 4, [[1,0],[2,0],[3,1],[3,2]]
# There are a total of 4 courses to take. To take course 3 you should 
# have finished both courses 1 and 2. Both courses 1 and 2 should be taken 
# after you finished course 0. So one correct course order is [0,1,2,3]. 
# Another correct ordering is[0,2,1,3].


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]

        Key: if cycle exists, can't finish course because depend on each other. (deadlock)
            Ex: A -> B -> A,  DFS: A -> B -> A    (x)
                A -> B <- C,  DFS: A -> B, C -> B (o)
        1. build graph info, include "visited" & "edge with direct" 
        2. start from unvisited vertex, do dfs visit, stop if next vertex visited.
        3. Ex: [4, [[1,0],[2,0],[3,1],[3,2]]]. start from 0: 0 -> (1, 2) -> (3, 3) 
        """
        
        # [visit status] 0: unvisited, 1: visited, 2: visiting, if visit again in this loop means cycle!
        visited = {v: 0 for v in range(numCourses)}
        # [build graph]
        graph = {v: [] for v in range(numCourses)}
        for s, e in prerequisites:
            graph[s].append(e)

        # [do dfs]
        def dfs(node):
            # print(visited)
            if visited[node] == 1:
                pass
            elif visited[node] == 2:
                return []
            elif visited[node] == 0:
                visited[node] = 2   # tracking
                for n in graph[node]:
                    if dfs(n) == []: return []
                visited[node] = 1
                ans.append(node)
                

        ans = []
        for n in range(numCourses):
            res = dfs(n)
            if res == []:
                return []
        return ans

        