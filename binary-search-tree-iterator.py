# Implement an iterator over a binary search tree (BST). 
# Your iterator will be initialized with the root node of a BST.

# Calling next() will return the next smallest number in the BST.

# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, 
# where h is the height of the tree.

# Definition for a binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator(object):

    # [Ideas]
    # 1. we can't use a full min heap since it need O(n) memory, 
    #    while it request O(h) memory
    # 2. do DFS but stop in current leftmost branch, 
    #    traverse more after each pop next!

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        res = self.stack.pop()
        root = res.right
        while root:
            self.stack.append(root)
            root = root.left
        print("res", res.val)
        return res.val
        

