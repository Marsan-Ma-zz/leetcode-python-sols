# https://leetcode.com/problems/inorder-successor-in-bst/

# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

# Note: If the given node has no in-order successor in the tree, return null.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        
        # [Ideas]
        # record parents from root, along the way till target(p)
        # if p has right-child => leftmost decendant in right branch
        # if not => find parent 
        #        => if through left branch, done
        #        => if through right branch, find even upper parent until is left branch
        
        if not root: return None
        
        ancestors = []
        node = root
        
        # find p
        while node:
            if node.val == p.val:
                break
            elif node.val > p.val:
                ancestors.append(node)
                node = node.left
            elif node.val < p.val:
                # ancestors.append(node)
                node = node.right
    
        if not node: return None
    
        # return successor
        if node.right:
            suc = node.right
            while suc.left:
                suc = suc.left
            return suc
        else:
            while ancestors:
                suc = ancestors.pop()
                if suc.val > p.val:
                    return suc
            return None
        