# https://leetcode.com/problems/minimum-height-trees/

# For a undirected graph with tree characteristics, we can choose 
# any node as the root. The result graph is then a rooted tree. 
# Among all possible rooted trees, those with minimum height are 
# called minimum height trees (MHTs). Given such a graph, write a 
# function to find all the MHTs and return a list of their root labels.

# Format
# The graph contains n nodes which are labeled from 0 to n - 1. 
# You will be given the number n and a list of undirected edges 
# (each edge is a pair of labels).

# You can assume that no duplicate edges will appear in edges. 
# Since all edges are undirected, [0, 1] is the same as [1, 0] and thus 
# will not appear together in edges.

# Example 1:

# Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

#         0
#         |
#         1
#        / \
#       2   3
# return [1]

# Example 2:

# Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

#      0  1  2
#       \ | /
#         3
#         |
#         4
#         |
#         5
# return [3, 4]

# Hint:

# How many MHTs can a graph have at most?
# Note:

# (1) According to the definition of tree on Wikipedia: “a tree is an 
# undirected graph in which any two vertices are connected by exactly 
# one path. In other words, any connected graph without simple cycles is a tree.”

# (2) The height of a rooted tree is the number of edges on the longest downward 
# path between the root and a leaf.



from collections import defaultdict
class Solution(object):
    
    # leaf cutting until <= 2 nodes (Hint: at most 2 MHT)
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not n: return []        
        if not edges: return [0]

        # build graph
        g = {k: set() for k in range(n)}
        for s, t in edges:
            g[s].add(t)
            g[t].add(s)


        # keep find and remove ends from graph
        while len(g) > 2:
            leafs = {k for k,v in g.items() if len(v) == 1}
            # gather neightbors
            neighbors = set()
            for a in leafs:
                neighbors |= g[a]
                del g[a] # remove nodes
            # remove links
            for nb in neighbors:
                g[nb] = {b for b in g[nb] if b not in leafs}
        return list(g.keys())
                    




    def test(self):
        cases = [
            (1, []),
            (4, [[1, 0], [1, 2], [1, 3]]),
            (6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]),
            (8, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4], [4, 7], [5, 6]]),
        ]
        for n, edges in cases:
            print(n, edges, self.findMinHeightTrees(n, edges))


# Solution().test()
