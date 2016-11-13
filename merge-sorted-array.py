# https://leetcode.com/problems/merge-sorted-array/

# Given two sorted integer arrays nums1 and nums2, merge 
# nums2 into nums1 as one sorted array.

# Note:
# You may assume that nums1 has enough space (size that is 
# greater or equal to m + n) to hold additional elements from nums2. 
# The number of elements initialized in nums1 and nums2 are m and n respectively.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # initialize
        ptr1, ptr2 = m-1, n-1
        # for n in nums2:
        #     nums1.append(-1)
            
        # fill nums1                           # idx  = [0,1,2,3,4,5,6]
        ptr = m+n-1                            # num1 = [1,1,3,5,_,_,_], num2 = [2,4,5], m=4, n=3, ptr=6
        while True: #(ptr1 >= 0) or (ptr2 >= 0):
            # print(ptr)
            # check complete
            if ptr1 == -1:
                nums1[:ptr+1] = nums2[:ptr2+1]
                break
            if ptr2 == -1:
                break
            # fill larger number
            # print(nums1, ptr, ptr1, ptr2)
            if nums1[ptr1] >= nums2[ptr2]:
                nums1[ptr] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[ptr] = nums2[ptr2]
                ptr2 -= 1
            ptr -= 1
            
        