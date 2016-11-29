# https://leetcode.com/problems/path-sum-iii/

# You are given a binary tree in which each node contains an integer value.

# Find the number of paths that sum to a given value.

# The path does not need to start or end at the root or a leaf, but it must 
# go downwards (traveling only from parent nodes to child nodes).

# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

# Example:

# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1

# Return 3. The paths that sum to 8 are:

# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import defaultdict


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # [Ideas]
        # 1. for each node, it’s a 2Sum problem from root to certain node
        # 2. use hashmap to record history acc so far, and the value just  
        #    memorize number of candidates rather than candidate value
        # 3. see how to “pop” current node value from hashmap   
        
        self.target, self.sol = sum, 0
        self.cache = defaultdict(int)
        self.cache[0] = 1  # “all the way from root” case
        self.dfs(root, 0)
        return self.sol


    def dfs(self, node, acc):
        if not node: return

        acc += node.val
        lack = acc - self.target
        self.sol += self.cache[lack]
        
        self.cache[acc] += 1
        self.dfs(node.left, acc)
        self.dfs(node.right, acc)
        self.cache[acc] -= 1
