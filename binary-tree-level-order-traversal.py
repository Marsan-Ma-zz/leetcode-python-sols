# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
# Show Company Tags
# Show Tags
# Show Similar Problems


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        
        [examples]
                3
               / \
              9  20
                /  \
               15   7
           
            [
              [3],
              [9,20],
              [15,7]
            ]
            
        [ideas]
            1. BFS, we might record value along with level info.
        
        """
        # boundary case
        if root == None: return []
        
        # BFS
        queue = [(root, 0)]
        last_level = 0
        ans = []
        this_row = []
        # queue: add deeper nodes from left, pop current node from right
        while queue: 
            node, level = queue.pop()
            if level == last_level:
                this_row.append(node.val)
            else: # dive deeper level
                last_level = level
                ans.append(this_row)
                this_row = [node.val]
            if node.left:
                queue = [(node.left, level+1)] + queue
            if node.right:
                queue = [(node.right, level+1)] + queue
                
        if this_row:
            ans.append(this_row)
        return ans
            
#     def unit_test(self):
#         root = TreeNode(3)
#         root.left = TreeNode(9)
#         root.right = TreeNode(20)

#         root.right.left = TreeNode(23)
#         root.right.right = TreeNode(34)
        
#         root.right.left = TreeNode(15)
#         root.right.right = TreeNode(7)
        
#         root.right.right.left = TreeNode(70)
#         root.right.right.right = TreeNode(80)
        
#         root.right.right.right.left = TreeNode(100)
        
#         ans = self.levelOrder(root)
#         print(ans)
        
        
# Solution().unit_test()