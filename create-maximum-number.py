# https://leetcode.com/problems/create-maximum-number/

# Given two arrays of length m and n with digits 0-9 representing two numbers. 
# Create the maximum number of length k <= m + n from digits of the two. 
# The relative order of the digits from the same array must be preserved. 
# Return an array of the k digits. You should try to optimize your time and 
# space complexity.


# Example 1:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# return [9, 8, 6, 5, 3]

# Example 2:
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
# return [6, 7, 6, 0, 4]

# Example 3:
# nums1 = [3, 9]
# nums2 = [8, 9]
# k = 3
# return [9, 8, 9]



class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        # [Ideas]
        # 1. select only in nums1 is relatively easy, just 
        #    always choose best MSB candidates for k time.
        # 2. combine two result from best of (i digit, nums1) 
        #    and (k-i digit, nums2) is easy, too.
        # 3. go through all combination of (i, k-i) and find max.
        
        def single_max(num, p): # should guarantee p <= len(num)
            sol = []
            while p:
                m = max(num[:len(num)-p+1])  # 01234, 3 => 23, 2
                sol.append(m)
                i = num.index(m)
                num = num[i+1:]
                p -= 1
            return sol
        
        
        def merge_max(n1, n2):
            sol = []
            while n1 + n2:
                if n1 > n2:  # python magic!! handle array compare
                # if n1 and ((not n2) or (n1[0] > n2[0])):
                    sol.append(n1.pop(0))
                else: # not n1 or n1[0] <= n2[0]
                    sol.append(n2.pop(0))
            return sol
        
            
        best = [0]
        for i in range(k+1):
            if i > len(nums1) or k-i > len(nums2): continue
            s1, s2 = single_max(nums1, i), single_max(nums2, k-i)
            sol = merge_max(s1, s2)
            # print(i, s1, s2, sol)
            if sol: best = max(best, sol)
        return best
    
    
    
    def test(self):
        cases = [
            ([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5),
            ([6, 7], [6, 0, 4], 5),
            ([3, 9], [8, 9], 3),
        ]
        for n1, n2, k in cases:
            print(self.maxNumber(n1, n2, k))
            
            
# Solution().test()
