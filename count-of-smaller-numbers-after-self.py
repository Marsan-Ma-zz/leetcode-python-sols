# https://leetcode.com/problems/count-of-smaller-numbers-after-self/

# You are given an integer array nums and you have to return a new counts array. 
# The counts array has the property where counts[i] is the number of smaller elements 
# to the right of nums[i].

# Example:

# Given nums = [5, 2, 6, 1]

# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# Return the array [2, 1, 1, 0].



class BinaryIndexedTree(object):

    def __init__(self, size):
        self.sums = [0] * (size+1)  # self.sums[0] is never used

    def update(self, i, val):
        while i < len(self.sums):
            self.sums[i] += val
            i += (i & -i)

    def sum(self, i):
        r = 0
        while i > 0:
            r += self.sums[i]
            i -= (i & -i)
        return r


    
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # 1. use BIT to count numbers "larger than i",
        #    and traverse nums in reverse order
        # 2. use a hash-table to re-index nums, 
        #    for reducing the number range in BIT
        #    Ex: [1, 8, 3] need BIT = [0,0,0,0,0,0,0,0,0]
        #    Ex: [1, 3, 2] only need BIT = [0,0,0,0]
        
        sol = []
        htbl = {k: i for i, k in enumerate(sorted(set(nums)))}
        bit = BinaryIndexedTree(len(htbl))
        
        for i in reversed(range(len(nums))):
            nn = htbl[nums[i]]    # hash-table replaced number
            sol.append(bit.sum(nn))
            bit.update(nn+1, 1)
            # print("bit:", bit.sums)
        return sol[::-1]
        
        
    def test(self):
        cases = [
            [],
            [1,4,6,8,5,3],
        ]
        for c in cases:
            print(c, self.countSmaller(c))
            
# Solution().test()