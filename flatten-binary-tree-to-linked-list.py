# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Given a binary tree, flatten it to a linked list in-place.

# For example,
# Given

#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6

             

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        # [Ideas]
        # 1. LIFO for right branches => stack
        if not root: return
    
        q = [root]
        last = None
        while q:
            node = q.pop()
            if node.right: 
                q.append(node.right)
            if node.left: 
                q.append(node.left)
            if last:
                last.right = node
            node.left, node.right = None, None
            last = node
                
            
            