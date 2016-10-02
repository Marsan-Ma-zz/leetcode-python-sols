# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/

# One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

#      _9_
#     /   \
#    3     2
#   / \   / \
#  4   1  #  6
# / \ / \   / \
# # # # #   # #
# For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

# Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

# Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

# You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

# Example 1:
# "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Return true

# Example 2:
# "1,#"
# Return false

# Example 3:
# "9,#,#,1"
# Return false


class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        
        # [Example]
        #      _9_
        #     /   \
        #    3     2
        #   / \   / \
        #  4   1  #  6
        # / \ / \   / \
        # # # # #   # #
        #
        # "9,3,4,#,#,1,#,#,2,#,6,#,#"
        #  1 2 3 2 1 2 1 0 1 0 1 0 -1 <= cnt
        
        # [Ideas]
        # 1. first item is the root => has 2 '#' quota
        # 2. maybe counting the '#' quota: for each number
        #    => begin child, create 1 more '#' quota
        #    => inorder traversal, '#' should always smaller than quota
        
        # 3. add up numbers is always valid
        # 4. focus on invalid '#' => out-of-quota
        # 5. other '#' coudision: 
        #    a) whole sequence should end up with '#'
        #    b) whole sequence '#' should be 1 more than numbers
        
        if not preorder: return False
        
        preorder = preorder.split(',')
        cnt = 0
        if preorder[-1] != '#':
            return False
        else:
            for n in preorder[:-1]:
                if n == '#':
                    cnt -= 1
                else:
                    cnt += 1
                if cnt < 0:
                    return False
        # print("cnt", cnt)
        return (cnt == 0)
            
            
    def test(self):
        cases = [
            '',
            '#',
            "1,#",
            "9,#,#,1",
            "9,3,4,#,#,1,#,#,2,#,6,#,#",
            "9,3,4,#,#,1,#,#,2,#,6,#",
            "9,3,4,#,#,1,#,#,2,#,6,#,3,4,#",
        ]
        for c in cases:
            print(c, self.isValidSerialization(c))
            
            
Solution().test()            