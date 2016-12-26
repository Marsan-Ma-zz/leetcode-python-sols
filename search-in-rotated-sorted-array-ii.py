# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?

# Would this affect the run-time complexity? How and why?

# Write a function to determine if a given target is in the array.


class Solution(object):
    
    def search(self, nums, target):

        # [Ideas]
        # 1. same as I, use binary search.
        # 2. [TRICK!!!] but first, eliminate all tail values equal to nums[0]
        #       to avoid confuse
        # 3. NOTE: search condition is tricky!

        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            while l < mid and nums[l] == nums[mid]: # tricky part
                l += 1
            # the first half is ordered
            if nums[l] <= nums[mid]:
                # target is in the first half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

        