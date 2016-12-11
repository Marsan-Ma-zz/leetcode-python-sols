# https://leetcode.com/problems/unique-binary-search-trees-ii/

# Given an integer n, generate all structurally unique BST's (binary search trees) 
# that store values 1...n.

# For example,
# Given n = 3, your program should return all 5 unique BST's shown below.

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n: return []
        
        def branch(nums):
            if not nums: return [None]
            sols = []
            for i in range(len(nums)):
                for l in branch(nums[:i]):
                    for r in branch(nums[i+1:]):
                        root = TreeNode(nums[i])
                        root.left = l
                        root.right = r
                        sols.append(root)
            return sols
    
        return branch(list(range(1, n+1)))
        