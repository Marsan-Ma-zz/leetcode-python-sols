# # https://leetcode.com/problems/binary-tree-vertical-order-traversal/

# Given a binary tree, return the vertical order traversal of its nodes' values. 
# (ie, from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.

# Examples:

# Given binary tree [3,9,20,null,null,15,7],
#    3
#   /\
#  /  \
#  9  20
#     /\
#    /  \
#   15   7
# return its vertical order traversal as:
# [
#   [9],
#   [3,15],
#   [20],
#   [7]
# ]
# Given binary tree [3,9,8,4,0,1,7],
#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7
# return its vertical order traversal as:
# [
#   [4],
#   [9],
#   [3,0,1],
#   [8],
#   [7]
# ]
# Given binary tree [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5),
#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7
#     /\
#    /  \
#    5   2
# return its vertical order traversal as:
# [
#   [4],
#   [9,5],
#   [3,0,1],
#   [8,2],
#   [7]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import defaultdict

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        # [Ideas]
        # do a DFS, remember how many times go left/right, 
        # then group by this score
        
        # boundary cases
        if not root: return []
        
        # BFS
        self.result = defaultdict(list)
        queue = [(root, 0)]
        while queue:
            node, score = queue.pop(0)
            self.result[score].append(node.val)
            if node.left:
                queue.append((node.left, score-1))
            if node.right:
                queue.append((node.right, score+1))
        
        return [v for k,v in sorted(self.result.items())]
        