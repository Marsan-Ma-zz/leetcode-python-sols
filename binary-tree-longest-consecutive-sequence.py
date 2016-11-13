# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/


# Given a binary tree, find the length of the longest consecutive sequence path.

# The path refers to any sequence of nodes from some starting node 
# to any node in the tree along the parent-child connections. 
# The longest consecutive path need to be from parent to child (cannot be the reverse).

# For example,
#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5
# Longest consecutive sequence path is 3-4-5, so return 3.
#    2
#     \
#      3
#     / 
#    2    
#   / 
#  1
# Longest consecutive sequence path is 2-3,not3-2-1, so return 2.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root: return 0
        
        self.sol = 0
        self.dfs(root, None, 0)
        return self.sol
    
    def dfs(self, node, last, level):
        # update seq
        if (last != None) and (node.val == (last + 1)):
            last, level = node.val, level+1
        else:
            last, level = node.val, 1
        self.sol = max(level, self.sol)
            
        # recursion
        if node.left:
            self.dfs(node.left, last, level)
        if node.right:
            self.dfs(node.right, last, level)
            