# https://leetcode.com/problems/third-maximum-number/

# Given a non-empty array of integers, return the third maximum number 
# in this array. If it does not exist, return the maximum number. 
# The time complexity must be in O(n).

# Example 1:
# Input: [3, 2, 1]

# Output: 1

# Explanation: The third maximum is 1.
# Example 2:
# Input: [1, 2]

# Output: 2

# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
# Example 3:
# Input: [2, 2, 3, 1]

# Output: 1

# Explanation: Note that the third maximum here means the third maximum distinct number.
# Both numbers with value 2 are both considered as second maximum.


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        m1 = m2 = m3 = -float('inf')
        for n in nums:
            if n > m1:
                m1, m2, m3 = n, m1, m2
            elif m1 > n > m2:
                m2, m3 = n, m2
            elif m2 > n > m3:
                m3 = n
                
        return m3 if m3 >= -2**31 else m1
        
        