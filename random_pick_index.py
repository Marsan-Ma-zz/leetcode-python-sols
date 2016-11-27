# https://leetcode.com/problems/random-pick-index/

# Given an array of integers with possible duplicates, randomly 
# output the index of a given target number. You can assume that 
# the given target number must exist in the array.

# Note:
# The array size can be very large. Solution that uses too much 
# extra space will not pass the judge.

# Example:

# int[] nums = new int[] {1,2,3,3,3};
# Solution solution = new Solution(nums);

# // pick(3) should return either index 2, 3, or 4 randomly. 
# Each index should have equal probability of returning.
# solution.pick(3);

# // pick(1) should return 0. Since in the array only nums[0] is equal to 1.
# solution.pick(1);


from collections import defaultdict
from random import choice

class Solution(object):
    
    
    # -----[Reservoir Sampling]----------
    # with probability 1/i, keep the new item (discard the old one)
    # with probability 1-1/i, keep the old item (ignore the new one)
    def __init__(self, nums):
        self.l = nums

    def pick(self, target):
        index,count,nums = -1,0,self.l
        for i in range(len(nums)):
            if nums[i] == target:
                if index == -1:
                    index = i
                elif random.randint(0,count) == 0:
                    index = i
                count += 1
        return index

        
    # -----[Hashmap]----------
    def __init__(self, nums):
        indexes = self.indexes = {}
        for i, num in enumerate(nums):
            I = indexes.get(num)
            if I is None:
                indexes[num] = i
            elif isinstance(I, int):
                indexes[num] = [I, i]
            else:
                indexes[num].append(i)

    def pick(self, target):
        I = self.indexes[target]
        return I if isinstance(I, int) else random.choice(I)

