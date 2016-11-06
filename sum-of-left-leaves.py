# https://leetcode.com/problems/sum-of-left-leaves/

# Find the sum of all left leaves in a given binary tree.

# Example:

#     3
#    / \
#   9  20
#     /  \
#    15   7

# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # [Ideas]
        # 1. do BFS, if left-leaf, accumulate
        
        if not root: return 0
        
        ans = 0
        queue = [(root, False)]
        while queue:
            node, isleft = queue.pop(0)
            if isleft and node.left == None and node.right == None:
                ans += node.val
            if node.left:
                queue.append((node.left, True))
            if node.right:
                queue.append((node.right, False))
                
        return ans
        