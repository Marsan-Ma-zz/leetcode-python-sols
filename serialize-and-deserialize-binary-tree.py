# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# For example, you may serialize the following tree

#     1
#    / \
#   2   3
#      / \
#     4   5
# as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
# Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    
    # [Ideas]
    # 1. use inorder + preorder => lousy decode, n*2 space
    # 2. preorder and mark every root-left-right pairs
    # 3. use raster scan with X
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = ''
        
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node:
                res += str(node.val) + ','
                stack += [node.left, node.right]
            else: # node == None
                res += 'X' + ','
        return res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # create head
        data = data.split(',')[:-1]
        if data[0] != 'X':
            head = TreeNode(int(data[0]))
            stack = [(head, 'l'), (head, 'r')]
        else:
            return None
        
        # build branches
        for n in data[1:]:
            parent, pos = stack.pop(0)
            # create node
            if n == 'X':
                node = None
            else:
                node = TreeNode(int(n))
                stack += [(node, 'l'), (node, 'r')]
            # update parent
            if pos == 'l':
                parent.left = node
            else: # pos == 'r'
                parent.right = node
        return head
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))