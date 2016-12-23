# https://leetcode.com/problems/clone-graph/

# Clone an undirected graph. Each node in the graph contains a label 
# and a list of its neighbors.

# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


class Solution:

    def cloneGraph(self, node):
        self.seen = {}
        if node:
            return self.cloneNode(node)
    

    def cloneNode(self, node):
        if node.label in self.seen:
            return self.seen[node.label]
        clonedNode = UndirectedGraphNode(node.label)
        clonedNode.neighbors = [self.cloneNode(n) for n in node.neighbors]
        self.seen[node.label] = clonedNode
        return clonedNode
        
# class Solution(object):
#     def cloneGraph(self, node):
#         """
#         :type node: UndirectedGraphNode
#         :rtype: UndirectedGraphNode
#         """

#         # [Ideas]
#         # 1. use a stack/queue to track unvisited node
#         # 2. use a set to track visited node
#         # 3. actually we use list in python for both

#         # boundary cases
#         if not node: return

#         mapper = {}     # map label to new node
#         completed = []  # processed nodes
#         stack = [node]  # nodes to process

#         # generate root node
#         nc = UndirectedGraphNode(node.label)
#         mapper[nc.label] = nc
#         head = nc

#         while stack:
#             # get node to process
#             n = stack.pop(0)
#             if n.label in completed: 
#                 continue
#             else:
#                 nc = mapper[n.label]

#             # collect neighbors
#             neighbors = []
#             for s in n.neighbors:
#                 if s.label not in mapper:
#                     sc = UndirectedGraphNode(s.label)
#                     mapper[sc.label] = sc
#                 else:
#                     sc = mapper[s.label]
#                 neighbors.append(sc)
#             nc.neighbors = neighbors
#             completed.append(nc.label)
#             stack += [t for t in n.neighbors if t.label not in completed]

#         return head

