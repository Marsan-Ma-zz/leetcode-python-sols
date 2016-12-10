# https://leetcode.com/problems/closest-binary-search-tree-value-ii/

# Given a non-empty binary search tree and a target value, find k values in the BST 
# that are closest to the target.

# Note:
# Given target value is a floating point.
# You may assume k is always valid, that is: k ≤ total nodes.
# You are guaranteed to have only one unique set of k values in the BST that are closest 
# to the target.

# Follow up:
# Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

# Hint:

# Consider implement these two helper functions:
# getPredecessor(N), which returns the next smaller node to N.
# getSuccessor(N), which returns the next larger node to N.
# Try to assume that each node has a parent pointer, it makes the problem much easier.
# Without parent pointer we just need to keep track of the path from the root to the current node 
# using a stack.
# You would need two stacks to track the path in finding predecessor and successor node separately.



from heapq import *

class Solution(object):

    def closestKValues(self, root, target, k):
        

        # [Ideas]
        # 1. traverse and use max-heap to keep k best value
        #    it's O(nlogk) ... 
        # 2. if we just do traversal then do binary search and find k,
        #    actially it's better ... O(n + log(n) + k) = O(n)
        # 3. there are better solution O(k*log(n)), but very tricky...
        #    https://discuss.leetcode.com/topic/22953/efficient-python

        def dfs(node):
            if node:
                diff = -abs(node.val - self.target)
                if len(self.heap) < k:
                    heappush(self.heap, (diff, node.val))
                elif diff > self.heap[0][0]:
                    heapreplace(self.heap, (diff, node.val))
                # print(self.heap)
                dfs(node.left)
                dfs(node.right)
        
        self.heap = []
        self.target = target
        dfs(root)
        return [heappop(self.heap)[1] for _ in range(k)][::-1]

