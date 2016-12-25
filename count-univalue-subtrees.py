# https://leetcode.com/problems/count-univalue-subtrees/

# Given a binary tree, count the number of uni-value subtrees.

# A Uni-value subtree means all nodes of the subtree have the same value.

# For example:
# Given binary tree,
#               5
#              / \
#             1   5
#            / \   \
#           5   5   5
# return 4.



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        self.sol = 0
        def helper(node):
            left = helper(node.left) if node.left else node.val
            right = helper(node.right) if node.right else node.val
            if node and (node.val == left == right):
                self.sol += 1
                return node.val
            else:
                return None
                
        helper(root)
        return self.sol
            
        
        