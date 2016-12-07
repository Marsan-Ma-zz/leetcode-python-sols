# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from 
# the root node down to the nearest leaf node.


# [Ideas]
# 1. do DFS to all leafs, only update sol on bottom leaves.
# 2. boundary case? 
#    => no branch, root only. ok.
#    => root only left branch. ok.
#    => root have both child. ok.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.shortest = float('inf')


        def dfs(node, depth):
            if not node: return
            new_depth = depth + 1
            if not node.left and not node.right:
                self.shortest = min(self.shortest, new_depth)
            else:
                dfs(node.left, new_depth)
                dfs(node.right, new_depth)
            
        dfs(root, 0)
        return self.shortest
