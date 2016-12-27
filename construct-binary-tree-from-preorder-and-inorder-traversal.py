# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Given preorder and inorder traversal of a tree, construct the binary tree.



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        if not preorder or not inorder: return None
        
        root = TreeNode(preorder.pop(0))
        pidx = inorder.index(root.val)
        
        root.left = self.buildTree(preorder, inorder[:pidx])
        root.right = self.buildTree(preorder, inorder[pidx+1:])
        return root