# https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/

# Given an array of numbers, verify whether it is the correct preorder traversal 
# sequence of a binary search tree.

# You may assume each number in the sequence is unique.

# Follow up:
# Could you do it using only constant space complexity?



class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        
        # [Ideas]
        # 1. preorder[0] is root. first number larger than it is right child.
        #    all left/right shall smaller/larger than root. 
        # 2. split into left/right branch, recursive.
        # 3. call by index instead of string, to save memory
        # X. still too slow
        # ----------------------------------------
        # 1. since it's a preorder traversal:
        #    => everytime with see value larger than last, 
        #       means left branch done, switch to right, thus:
        #    => shall not see any value smaller than parent
        
        stack, low = [], -float('inf')
        for p in preorder:
            if p < low:
                return False
            while stack and stack[-1] < p:
                low = stack.pop()
            stack.append(p)
        return True
        
        
        # nums = preorder
        
        # def verify(a, b):
        #     if a == b: return True
        #     root = nums[a]
        #     rchild = None
        #     for i in range(a+1, b):
        #         if nums[i] > root and rchild == None:
        #             rchild = i
        #         elif nums[i] < root and rchild != None:
        #             return False
        #     rchild = rchild or b
        #     return verify(a+1, rchild) and verify(rchild, b)
        
        # return verify(0, len(nums))
                    
    def test(self):
        cases = [
            [],
            [1],
            [1,2,3,4],
            [4,1,2,3,4,5,6,7],
            [4,1,2,3,4,5,6,7,3],
        ]
        for c in cases:
            print(c, self.verifyPreorder(c))
            
# Solution().test()