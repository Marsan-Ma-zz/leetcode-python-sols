# https://leetcode.com/problems/next-permutation/

# Implement next permutation, which rearranges numbers into the 
# lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the 
# lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place, do not allocate extra memory.

# Here are some examples. Inputs are in the left-hand column and 
# its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        if not nums: return
        
        # [Ideas]
        # 1. nextPermutation means to pivot by the first decending point
        #    1,2,3,4,5,3,2 => 1,2,3,5,2,3,4
        #          ~~~~~~~          ~~~~~~~
        #    where swap (4,5) and cascade sorted(4,4,3)
        # 2. we don't need to really "sort" (4,4,3) which cost O(nlog(n))
        #    we just need to reverse it
        # 3. [WARNING!!] a = a[::-1] CANNOT reverse inplace! 
        #    since [:] spliting will create new list
        #    thus we need a reverse() func to do the trick.
        
        
        # find pivot point
        l = len(nums)
        for j in range(1, l):  # 1 to l-1
            i = l-1-j  # l-2 to 0
            if nums[i] < nums[i+1]:
                # find smallest d among nums[i+1:] which > nums[i]
                next_lead = i+1
                while next_lead < l-1:
                    if nums[next_lead+1] > nums[i]:
                        next_lead += 1
                    else:
                        break
                nums[i], nums[next_lead] = nums[next_lead], nums[i] # swap
                
                # reverse rest
                self.reverse(nums, start=i+1) #nums[i+1:][::-1]
                return
            
        self.reverse(nums) #nums[::-1]
        return
        # print(nums)
    
    # inplace reverse list
    def reverse(self, nn, start=0):
        ll = len(nn) - start
        for i in range(ll//2):
            nn[start+i], nn[start+ll-1-i] = nn[start+ll-1-i], nn[start+i]
    
    
    def test(self):
        cases = [
            [],
            [1,2,3],
            [3,2,1],
            [1,1,5],
            [1,1,5,1],
            [1,2,5],
            [1,3,2],
            [1,2,3,5,4,2,1],
        ]
        for c in cases:
            d = c[:] 
            self.nextPermutation(d)
            print(c, d)
            
            
# Solution().test()
