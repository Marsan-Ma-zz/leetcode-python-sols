# https://leetcode.com/problems/maximum-product-subarray/

# Find the contiguous subarray within an array (containing at least one number) 
# which has the largest product.

# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.



class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # [Examples]
        # 1. [2,3,-2,4] => [2, 3] = 6
        
        # [Ideas]
        # 1. always keep 2 extreme candidates: max and min, 
        #    for negative min might multiply with negative 
        #    and turn into max
        
        ma, mi = nums[0], nums[0]
        best = nums[0]
        for n in nums[1:]:
            ma, mi = max(ma*n, mi*n, n), min(ma*n, mi*n, n)
            best = max(best, ma)
        return best
    
    
    def test(self):
        cases = [
            # [1],
            [-4,-3,-2],
            # [2,3,-2,4],
            # [2,3,-2,4,2,3,-2,4],
            # [2,3,-2,4,2,3,0,-2,4],
            # [2,3,-2,0,4,2,3,-2,4],
        ]
        for c in cases:
            print(c, self.maxProduct(c))
            
            
# Solution().test()