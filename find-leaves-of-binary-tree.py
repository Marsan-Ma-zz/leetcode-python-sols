# https://leetcode.com/problems/find-leaves-of-binary-tree/

# Given a binary tree, collect a tree's nodes as if you were doing this: 
# Collect and remove all leaves, repeat until the tree is empty.

# Example:
# Given binary tree 
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# Returns [4, 5, 3], [2], [1].

# Explanation:
# 1. Removing the leaves [4, 5, 3] would result in this tree:

#           1
#          / 
#         2          
# 2. Now removing the leaf [2] would result in this tree:

#           1          
# 3. Now removing the leaf [1] would result in the empty tree:

#           []         
# Returns [4, 5, 3], [2], [1].



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import defaultdict


class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # [Ideas]
        # DFS, propagate child depth to be current node level


        tbl = defaultdict(list)


        def dfs(node):
           if not node:
               return 0
           if not node.left and not node.right:
               level = 1
           else:
               d1 = dfs(node.left) if node.left else 0
               d2 = dfs(node.right) if node.right else 0
               level = max(d1, d2) + 1
           tbl[level].append(node.val)
           return level
        
        deepest = dfs(root)
        sols = []
        for i in range(deepest+1):
            if tbl[i]: sols.append(tbl[i])
        return sols
