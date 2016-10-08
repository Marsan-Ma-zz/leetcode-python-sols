# https://leetcode.com/problems/sort-transformed-array/

# Given a sorted array of integers nums and integer values a, b and c. Apply a function of the form f(x) = ax2 + bx + c to each element x in the array.

# The returned array must be in sorted order.

# Expected time complexity: O(n)

# Example:
# nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,

# Result: [3, 9, 15, 33]

# nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5

# Result: [-23, -5, 1, 7]


class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        
        # [Examples]
        # nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,
        #    Result: [3, 9, 15, 33]
        # nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5
        #    Result: [-23, -5, 1, 7]
        
        # [Ideas]
        # 1. Expected time complexity: O(n) => can't sort
        #    have to know the sorted order prior to evaluating.
        # 2. since a,b,c and nums are integers => > 1 
        #    => don't need to consider x**2 < x
        # 3. be aware of the sign!
        # 4. suppose ax**2 always dominate, then bx, c is useless
        #    => solve ax**2 = bx to get region delimiter
        # 5. even we know result ordering before calculation, 
        #    how do we arrange appropriate input order (nums) in O(n) ?
        #    => nums is sorted
        #    => abs(bx) will follow this sorted order
        #    => ax**2 will not follow, but could be collected by:
        #       alternatively append result in head/tail of results?
        #---------------------------
        # 1. just evaluate in nums original sorted order, but
        #    append result to head/tail according to the sign
        # 2. suppose we have [-100, -4, -2, 2, 3, 4], a=b=c=1
        #              sol = [9901, 13,  3, 7,13,21] 
        #    => do -100 first, then 4, then -4, 3, 2, -2
        #    => how do we know the order of -4 and 3?
        # 3. we could know k = ax + b in O(n), which follow same order
        #    => how do we know the order of kx ?
        #---------------------------
        # 1. evaluate all sign < 0 inputs in O(n) 
        #    by alternatively append result in head/tail of result
        # 2. evaluate all sign >= 0 inputs, the order remain the same.
        # 3. merge this two result is easy to be O(n)
        
        if a == 0:
            ans = [a*n**2+b*n+c for n in nums]
            if b < 0:
                return list(reversed(ans))
            else:
                return ans
        
        # dispatch
        nums1, nums2 = [], [] 
        th = -float(b)/(2*a)
        for n in nums: 
            if n >= th:
                nums1.append(n)
            else:
                nums2.append(n)
        print(nums1, nums2)
        res1 = [a*n**2+b*n+c for n in nums1]
        res2 = [a*n**2+b*n+c for n in nums2]
        
        
        if a >= 0:
            res2 = list(reversed(res2))
        else: # a < 0
            res1 = list(reversed(res1))
        # print(res1, res2)
#         # process
#         # res1 = [a*n**2+b*n+c for n in nums1]
#         res1 = []
#         for n in nums1:
#             sol = a*n**2+b*n+c
#             if sol >= 0:
#                 res1.append(sol)
#             else:
#                 res1 = [sol] + res1
        
#         res2 = []
#         for n in reversed(nums2):
#             sol = a*n**2+b*n+c
#             if sol >= 0:
#                 res2.append(sol)
#             else:
#                 res2 = [sol] + res2
        
        
        # merge
        i1, i2, i = 0, 0, 0
        while i1 < len(res1) and i2 < len(res2):
            if res1[i1] <= res2[i2]:
                nums[i] = res1[i1]
                i1 += 1
            else:
                nums[i] = res2[i2]
                i2 += 1
            i += 1
        while i1 < len(res1):
            nums[i] = res1[i1]
            i1 += 1
            i += 1
        while i2 < len(res2):
            nums[i] = res2[i2]
            i2 += 1
            i += 1
        return nums
    
    
    def test(self):
        cases = [
            # ([], 1,2,3),
            # ([-4, -2, 2, 4], 1, 3, 5),
            # ([-4, -2, 2, 4], -1, 3, 5),
            ([-4, -3, -2, -1, 0, 1, 2, 3, 4], -1, 3, 5),
            ([-4, -3, -2, -1, 0, 1, 2, 3, 4], -1, -3, 5),
            ([-4, -3, -2, -1, 0, 1, 2, 3, 4], 1, -3, 5),
            ([-4, -3, -2, -1, 0, 1, 2, 3, 4], 1, 3, 5),
        ]
        for nums, a, b, c in cases:
            sol = self.sortTransformedArray(nums[:], a, b, c)
            correct = sorted([a*x**2+b*x+c for x in nums])
            # print(nums, a, b, c, sol, sol==correct)
                
        
        
# Solution().test()
# print(2*3**2)