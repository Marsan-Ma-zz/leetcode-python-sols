# https://leetcode.com/problems/delete-node-in-a-bst/

# Given a root node reference of a BST and a key, delete the node with the 
# given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.
# Note: Time complexity should be O(height of tree).

# Example:

# root = [5,3,6,2,4,null,7]
# key = 3

#     5
#    / \
#   3   6
#  / \   \
# 2   4   7

# Given key to delete is 3. So we find the node with value 3 and delete it.

# One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

#     5
#    / \
#   4   6
#  /     \
# 2       7

# Another valid answer is [5,2,6,null,4,null,7].

#     5
#    / \
#   2   6
#    \   \
#     4   7



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        
        # search
        last, dir = None, None
        node = root
        while node and node.val != key:
            last = node
            if node.val > key:
                node = node.left
                dir = 0
            else: # node.val < key:
                node = node.right
                dir = 1
        if not node: return root
        # print(last.val, node.val, dir)
        
        # delete node
        new_node = None  # if node has no child
        if node.right:
            new_node = node.right
            bottom = new_node
            while bottom.left:
                bottom = bottom.left
            bottom.left = node.left
        elif node.left:
            new_node = node.left
            bottom = new_node
            while bottom.right:
                bottom = bottom.right
            bottom.right = node.right
            
        # connect new_node with parent
        if last:
            if dir == 0:
                last.left = new_node
                # print(last.val, new_node.val)
            else:
                last.right = new_node
            return root
        else: # root is deleted
            return new_node
        