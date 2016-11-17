# https://leetcode.com/problems/median-of-two-sorted-arrays/

# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. 
# The overall run time complexity should be O(log (m+n)).

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5


from bisect import bisect_left

class Solution(object):
    
    # explain: https://discuss.leetcode.com/topic/33430/6-lines-o-log-min-m-n-ruby

    # [Ideas]
    # 1. suppose l = (len(nums1)+len(nums2)) / 2
    #    pick any number nums1[i] will refer to nums2[l-i] are 
    #    consecutive if nums1 and nums2 are merged
    # 2. so we use binary search to find this "i" that make nums2[l-i] follow rules

    def findMedianSortedArrays(self, nums1, nums2):
        a, b = sorted((nums1, nums2), key=len)
        m, n = len(a), len(b)
        after = (m + n - 1) // 2
        lo, hi = 0, m
        while lo < hi:
            i = (lo + hi) // 2
            if after-i-1 < 0 or a[i] >= b[after-i-1]:
                hi = i
            else:
                lo = i + 1
        i = lo
        nextfew = sorted(a[i:i+2] + b[after-i:after-i+2])
        return (nextfew[0] + nextfew[1 - (m+n)%2]) / 2.0
        
        
    def test(self):
        cases = [
            [[1,3], [2]],
            [[1,2], [3,4]],
        ]
        for n1, n2 in cases:
            print(n1, n2, self.findMedianSortedArrays(n1, n2))

            
Solution().test()
