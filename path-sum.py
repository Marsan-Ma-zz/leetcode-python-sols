# https://leetcode.com/problems/path-sum/

# Given a binary tree and a sum, determine if the tree has a root-to-leaf 
# path such that adding up all the values along the path equals the given sum.

# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.sum = sum
        self.sol = False
        self.dfs(root, 0)
        return self.sol
        
        
    def dfs(self, node, acc):
        if self.sol or not node: return
        val = acc + node.val
        if not node.left and not node.right and val == self.sum:
            self.sol = True
        self.dfs(node.left, val)
        self.dfs(node.right, val)


