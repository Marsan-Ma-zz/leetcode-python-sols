# # https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

# Follow up for problem "Populating Next Right Pointers in Each Node".

# What if the given tree could be any binary tree? Would your previous solution still work?

# Note:

# You may only use constant extra space.
# For example,
# Given the following binary tree,
#          1
#        /  \
#       2    3
#      / \    \
#     4   5    7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \    \
#     4-> 5 -> 7 -> NULL


# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        
        # [Ideas]
        # 1. do a bfs and keep last node in the same height
        
        if not root: return
        
        lnode, lrank = None, -1    # last node/rank
        queue = [(root, 0)]
        while queue:
            node, rank = queue.pop(0)
            
            # update last node "next" pointer
            if lnode and (lrank == rank):
                lnode.next = node
            lnode, lrank = node, rank
            
            # push children in queue
            if node.left:
                queue.append((node.left, rank+1))
            if node.right:
                queue.append((node.right, rank+1))
            
        