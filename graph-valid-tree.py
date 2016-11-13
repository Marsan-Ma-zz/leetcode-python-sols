# https://leetcode.com/problems/graph-valid-tree/

# Given n nodes labeled from 0 to n - 1 and a list of undirected edges 
# (each edge is a pair of nodes), write a function to check whether 
# these edges make up a valid tree.

# For example:

# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

from collections import defaultdict

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        
        1. tree => undirected, no cycles 
           => do DFS, expect all nodes has only 1 "depth", no nodes should be visited twice. (time cost: O(nodes))
        2. before DFS, have to construct a hashmap to record all connections. (time cost: O(edges))
        """
        # boundary case
        if n == 0: return False
        
        # construct connection map
        conns = defaultdict(list)   # n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
        for n1, n2 in edges:                 
            conns[n1].append(n2)
            conns[n2].append(n1)
        # print(conns)                         # conns = {0: [1,2,3], 1:[0,4], 2:[0], 3:[0], 4:[1]} 
        
        # DFS
        stack = [0]
        visited = {i: 0 for i in range(n)}   # visited = {0:0, 1:0, 2:0, 3:0, 4:0}
        while stack:                         # stack = [0,1,2,3,4]
            node = stack.pop()
            visited[node] += 1
            if visited[node] > 1: 
                return False
            else:
                if node in conns:
                    for i in conns[node]:
                        stack += [i]
                        conns[i].remove(node)   # remove traced edge, don't traverse back
        # print(visited)
        
        # check visited count, should all be 1
        for k,v in visited.items():
            if v != 1: 
                return False
        return True
            