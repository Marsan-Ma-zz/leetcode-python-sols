# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Given inorder and postorder traversal of a tree, construct the binary tree.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        # [Ideas]
        # 1. postorder: get root from tail
        #    inorder: use the root to separate left-right branch
        # 2. separate left/right for next iteration:
        #    => inorder: separate by root
        #    => postorder: root.left would be end of left branch,
        #       where root.left is 
        #-------------------------
        # 1. how to split post-order tree?
        #    => actually don't need to!! see following sol!!  
        
        if not inorder or not postorder: return None
        root = TreeNode(postorder.pop())
        pidx = inorder.index(root.val)
        
        root.right = self.buildTree(inorder[pidx+1:], postorder)
        root.left = self.buildTree(inorder[:pidx], postorder)
            
        return root
                    
            
            