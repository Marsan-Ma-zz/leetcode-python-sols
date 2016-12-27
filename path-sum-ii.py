# https://leetcode.com/problems/path-sum-ii/

# Given a binary tree and a sum, find all root-to-leaf paths where each path's 
# sum equals the given sum.

# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        self.sols = []
        def dfs(node, val, items):
            if not node: return
            new_val = val + node.val
            new_items = items + [node.val]
            if not node.left and not node.right: 
                if new_val == sum:
                    self.sols.append(new_items)
            if node.left:
                dfs(node.left, new_val, new_items)
            if node.right:
                dfs(node.right, new_val, new_items)
            
        dfs(root, 0, [])
        return self.sols