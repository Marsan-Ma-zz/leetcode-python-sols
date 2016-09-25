# https://leetcode.com/problems/validate-binary-search-tree/

# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:
#     2
#    / \
#   1   3
# Binary tree [2,1,3], return true.
# Example 2:
#     1
#    / \
#   2   3
# Binary tree [1,2,3], return false.

# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    valid_flag = True
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def checkBSTrange(node):
            if not self.valid_flag:
                return (None, None)
            if not node:
                return (None, None)
            else:
                left_min, left_max = checkBSTrange(node.left)
                right_min, right_max = checkBSTrange(node.right)
                if not self.valid_flag: return (None, None)
                # print(node.val, left_min, left_max, right_min, right_max)
                if (left_max != None) and (left_max >= node.val):
                    self.valid_flag = False
                elif (right_min != None) and (right_min <= node.val):
                    self.valid_flag = False

            return ((left_min or node.val), (right_max or node.val))

        if not root:
            return True
        else:
            checkBSTrange(root)
            return self.valid_flag
        
        