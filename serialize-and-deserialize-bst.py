# https://leetcode.com/problems/serialize-and-deserialize-bst/

# Serialization is the process of converting a data structure or object into a sequence 
# of bits so that it can be stored in a file or memory buffer, or transmitted across a 
# network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary search tree. There is no 
# restriction on how your serialization/deserialization algorithm should work. 
# You just need to ensure that a binary search tree can be serialized to a string and 
# this string can be deserialized to the original tree structure.

# The encoded string should be as compact as possible.

# Note: Do not use class member/global/static variables to store states. 
# Your serialize and deserialize algorithms should be stateless.



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        sols = []
        q = deque([root])
        while q:
            node = q.popleft()
            v = str(node.val) if node else '#'
            sols.append(v)
            if node:
                q.extend([node.left, node.right])
        return ','.join(sols)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = deque(data.split(','))
        root, flag = None, False
        q = deque([])
        while data:
            val = data.popleft()
            node = TreeNode(int(val)) if val.isdigit() else None
            if not root: root = node
            
            # append to child
            if q: # if root, no parent
                if flag: # append to cur node right child
                    q[0].right = node
                    q.popleft()
                else: # append to cur node left child
                    q[0].left = node
                flag = not flag
            
            # append node to queue for later process
            if node: q.append(node)
            
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))