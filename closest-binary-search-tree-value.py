# https://leetcode.com/problems/closest-binary-search-tree-value/

# Given a non-empty binary search tree and a target value, 
# find the value in the BST that is closest to the target.

# Note:
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that 
# is closest to the target.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        
        # [Ideas]
        # 1. do binary-search-tree traverse until nothing to go
        # 2. check all the path as candidates
        # 3. prove: each time we choose path, 
        #     => we actually abandom opponent subtree
        #     => possible candidates: passed node and current branch
        #     => thus if we traverse to nowhere to go
        #     => nodes been go through is the only cadidates
        
        
        if not root: return None
        
        # find v1
        node = root
        cands = [node.val]
        while node:
            if node.val == target:
                return node.val
            elif (node.val < target) and (node.right):
                node = node.right
                cands.append(node.val)
            elif (node.val > target) and (node.left):
                node = node.left
                cands.append(node.val)
            else:
                break
             
        # print(cands)
        cidx = sorted([(abs(c-target), i) for i, c in enumerate(cands)])[0][1]
        return cands[cidx]
    