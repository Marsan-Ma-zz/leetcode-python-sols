# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

# Given a non-empty integer array, find the minimum number of moves required to 
# make all array elements equal, where a move is incrementing a selected element 
# by 1 or decrementing a selected element by 1.

# You may assume the array's length is at most 10,000.

# Example:

# Input:
# [1,2,3]

# Output:
# 2

# Explanation:
# Only two moves are needed (remember each move increments or decrements one element):

# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]



class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # [Ideas]
        # 1. move toward average?
        #    X. imageine [0,0,0,0,0,0,0,0,0,100] => 100 vs (89+ 10*9)
        # 2. move toward medium? 
        #    => suppose we have some solution
        #    => move up/down, if +/- nums are not equal, always have 
        #       one direction better until +/- nums are equal
        #    => so it's medium!
        # 3. better way to move and update?
        #    => start from diff with max, move downward
        #       use min-heap to maintain how many numbers are smaller
        #       and how many are larger than current threshold
        #    => O(n*log(n))
        # 4. minimize |x-a1| + |x-a2| + ... |x-an| => no sol
        
        
        nums = sorted(nums)
        med = nums[len(nums)//2]
        if len(nums)&1:
            med = nums[len(nums)//2]
        else:
            med = (nums[len(nums)//2-1] + nums[len(nums)//2])//2
        
        return sum(abs(n-med) for n in nums)
        
    def test(self):
        cases = [
            # [],
            [1,3,2],
            [0,0,0,0,0,0,0,0,0,100],
        ]
        for c in cases:
            print(c, self.minMoves2(c))
            
# Solution().test()