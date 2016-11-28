# https://leetcode.com/problems/binary-tree-paths/

# Given a binary tree, return all root-to-leaf paths.

# For example, given the following binary tree:

#    1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:

# ["1->2->5", "1->3"]



class Solution:
    
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        
        # [Idea]
        # 1. DFS, append path to solutions if reach end child
        # 2. use stack to do DFS, saving deep function call stack of recursion.

        # boundary case handling 
        if not root: return []

        self.results = []
        self.dfs(root, [])
        return self.results


    def dfs(self, root, s):
        path = s + [root.val]
        if root.left:
            self.dfs(root.left, path)
        if root.right:
            self.dfs(root.right, path)
        if (not root.left) and (not root.right):
            self.results.append("->".join([str(p) for p in path]))


