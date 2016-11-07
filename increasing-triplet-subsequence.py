# https://leetcode.com/problems/increasing-triplet-subsequence/

# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

# Formally the function should:
# Return true if there exists i, j, k 
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
# Your algorithm should run in O(n) time complexity and O(1) space complexity.

# Examples:
# Given [1, 2, 3, 4, 5],
# return true.

# Given [5, 4, 3, 2, 1],
# return false.


class Solution(object):
    # for triplet, O(n)
    def increasingTriplet(self, nums):
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
    

    # [generalize to k subsequency, O(n*log(n))]
    def increasingSubsequence(self, nums, k):
        inc = [float('inf')] * (k - 1)
        for x in nums:
            i = bisect.bisect_left(inc, x)
            if i >= k - 1:
                return True
            inc[i] = x
        return k == 0
#     def increasingTriplet(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
        
#         # [Ideas]
#         # 1. brute force: traverse all triplet and verify: O(n**3)
#         # 2. if first number chosen, then find ascenging in it's right side
#         # 3. one-pass check for "whether ascenging exists in righthand side"
#         #    and the smaller number of ascending
#         # 4. one-pass check for "minimum value in left-hand side"
#         # 5. one-pass check for "righthand have ascending, and also 
#         #    got left-hand min < right hand side minimum value
#         #    
        
        
        
#         # min in left hand side
#         min_val, left_min = None, []
#         for i in range(len(nums)):
#             if (min_val == None) or (nums[i] < min_val):
#                 min_val = nums[i]
#             left_min.append(min_val)
                       
#         # ascending and min of ascending
#         min_val, max_val = None, None
#         asc_min = []
#         check = False
#         for i in reversed(range(len(nums))):
#             if max_val == None or nums[i] > max_val:
#                 max_val = nums[i]
#             if max_val != None and nums[i] < max_val:
#                 if min_val != None:
#                     min_val = max(min_val, nums[i])
#                 else:
#                     min_val = nums[i]
#             if min_val != None:
#                 check = True
                
#             if check:
#                 if min_val:
#                     asc_min = [min_val] + asc_min
#                 elif nums[i] < max_val:
#                     asc_min = [nums[i]] + asc_min
#                 else:
#                     asc_min = [None] + asc_min
#             else:
#                 asc_min = [None] + asc_min
                       
#         # merge
#         print(left_min, asc_min)
#         if asc_min and (asc_min[0] != None):
#             for i in range(len(nums)):
#                 if (asc_min[i] != None) and (left_min[i] < asc_min[i]):
#                     return True
#             return False
#         else:
#             return False
            
        
        
                       
                       
#     def test(self):
#         cases = [
#             [],
#             [1,2,3,4,5],
#             [10,2,30,4,5],
#             [100,20,30,4,5],
#             [5,4,3,2,1],
#             [1,2,3,1,2,1],
#         ]
#         for c in cases:
#             print(c, self.increasingTriplet(c))
                 
                       
# # Solution().test()
# # print(max(None, 3))