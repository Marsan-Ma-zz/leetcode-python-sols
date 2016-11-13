# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

# Given n nodes labeled from 0 to n - 1 and a list of undirected edges 
# (each edge is a pair of nodes), write a function to find the number of 
# connected components in an undirected graph.

# Example 1:
#      0          3
#      |          |
#      1 --- 2    4
# Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

# Example 2:
#      0           4
#      |           |
#      1 --- 2 --- 3
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.



class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        # [Ideas]
        # 1. build graph using dict, 
        #    which could trace from both sides of edge
        # 2. traverse through connected nodes as 1 group
        
        graph = {k: [] for k in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        gcnt = 0
        for i in range(n):
            if i in graph: 
                gcnt += 1
                stack = graph[i]
            while stack:
                cur = stack.pop()
                if cur not in graph: continue
                stack += [c for c in graph[cur] if c in graph]
                del graph[cur]
                
        return gcnt
    
    
    def test(self):
        cases = [
            (5, []),
            (5, [[0, 1], [1, 2], [3, 4]]),
            (5, [[0, 1], [1, 2], [2, 3], [3, 4]]),
        ]
        for n, edges in cases:
            print(n, edges, self.countComponents(n, edges))
                    
        
# Solution().test()