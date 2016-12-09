# https://leetcode.com/problems/patching-array/

# Given a sorted positive integer array nums and an integer n, 
# add/patch elements to the array such that any number in range [1, n] 
# inclusive can be formed by the sum of some elements in the array. 
# Return the minimum number of patches required.

# Example 1:
# nums = [1, 3], n = 6
# Return 1.

# Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
# Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
# Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
# So we only need 1 patch.

# Example 2:
# nums = [1, 5, 10], n = 20
# Return 2.
# The two patches can be [2, 4].

# Example 3:
# nums = [1, 2, 2], n = 5
# Return 0.



class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        
        # [Examples]
        # nums = [1, 3], n = 6 => add [2]
        # nums = [1, 5, 10], n = 20 => add [2, 4]
        # nums = [1, 2, 2], n = 5 => no need to add
        
        # [Ideas]
        # 1. DP from 1 to n, for any number 1 <= i <= n,
        #    as long as i - n fail in a number could be composed of 
        #    other unused number, pass.
        # 2. bottom-up DP will not waste time since we need all numbers
        # 3. if we lack i, just add i would be better?
        #    => prevent adding [... 1,1,1,1] or [...i,i+1,i+2]
        # -----------------------------------------
        # 1. for nums able to comb 1_to_n, only n+1 needed, 
        #    to comb from 1_to_2n+1
        # 2. if there are m in 1~n and others could comb 1_to_n, 
        #    then with m they are 1_to_n+m
        #    Ex: [1,2,4] comb 1_to_7, add 5 make them 1_to_12
        #        since 5 + 3_to_7 = 8_to_12
        # 3. Conclusion: DP from 1 to n, if i is unreachable, 
        #    always add i in comb!
        # 4. sort nums, from smallest to check reachable numbers
        
        nums.sort()
        added = 0
        
        ptr, target = 0, 1 
        while target < n+1:
            # add number
            if ptr >= len(nums):
                added += 1
                target = target << 1
            else:
                # use existing
                top = nums[ptr]
                if top == target:
                    target = target << 1
                    ptr += 1
                elif top < target:
                    target += top
                    ptr += 1
                else: # top > target:
                    added += 1
                    target = target << 1
        return added
    
    def test(self):
        cases = [
            ([], 7),
            ([1, 3], 6),
            ([1, 5, 10], 20),
            ([1, 2, 2], 5),
        ]
        for nums, k in cases:
            print(nums, k, self.minPatches(nums, k))
    
    
# Solution().test()