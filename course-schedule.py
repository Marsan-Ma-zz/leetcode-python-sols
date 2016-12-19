# https://leetcode.com/problems/course-schedule/

# There are a total of n courses you have to take, labeled from 0 to n - 1.

# Some courses may have prerequisites, for example to take course 0 you have to first 
# take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible 
# for you to finish all courses?

# For example:

# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. 
# So it is possible.

# 2, [[1,0],[0,1]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0, 
# and to take course 0 you should also have finished course 1. So it is impossible.

# Note:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. 
# Read more about how a graph is represented.



from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        suc, pre = defaultdict(set), defaultdict(set)
        free = {n for n in range(numCourses)}
        for a, b in prerequisites:
            suc[b].add(a)
            pre[a].add(b)
            if a in free: free.remove(a)
        
        visited = set()
        free = list(free)
        for c in free:
            if c in visited: continue
            visited.add(c)
            for s in suc[c]:
                pre[s].remove(c)
                if not pre[s]: free.append(s)
            
        return len(visited) == numCourses