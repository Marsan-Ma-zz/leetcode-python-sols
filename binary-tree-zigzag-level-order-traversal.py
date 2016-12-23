# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Given a binary tree, return the zigzag level order traversal of its nodes' values. 
# (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        
        q = deque([root])
        sol = []
        while q:
            row = []
            for _ in range(len(q)):
                node = q.popleft()
                row.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if len(sol) % 2 == 1: row = row[::-1]
            sol.append(row)
        return sol
        