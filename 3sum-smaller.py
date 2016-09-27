# https://leetcode.com/problems/3sum-smaller/

# Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

# For example, given nums = [-2, 0, 1, 3], and target = 2.

# Return 2. Because there are two triplets which sums are less than 2:

# [-2, 0, 1]
# [-2, 0, 3]
# Follow up:
# Could you solve it in O(n2) runtime?

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # [Ideas]
        # 1. brute force: O(n**3) to traverse all possible combs, but:
        #    a) sort nums first, then choose from small to large
        #    b) break branch while sum >= target
        # 2. don't memorize combination, just count-up final_sols
        # 3. choose 1st number,=> than the rest become 2-sum =>
        #    could achieve within O(n) by 2-pointer shifting
        
        # [inspect cases]
        # [-2, 0, 1, 3], and target = 2.
        # 1. choose -2 => choose 2 in [0,1,3] which sum < 4
        #    too simple, use another case:
        # 2. suppose choose 2 in [0,1,2,3,4,5] which sum < 3:
        #    start from (0, 5) => (0, 4) => (0, 3) => (1, 3) => (1,2)
        #    where                          +3                  +1
        
        if not nums: return 0
        
        nums = sorted(nums)
        sols = 0
        
        for i1, n1 in enumerate(nums):    # first number
            p1, p2 = i1+1, len(nums)-1
            ta = target - n1
            while True:
                if (p1 >= p2): break
                if nums[p1] + nums[p2] < ta:
                    sols += p2-p1
                    p1 += 1
                else:
                    p2 -= 1

        return sols    
            
    def test(self):
        cases = [
            ([], 1),
            ([-2, -1, 0], 1),
            ([1, 2, 3, 4, 5], 5),
            ([-2, 0, 1, 3], 2),
            ([-2, 0, 1, 2, 3], 3),
        ]
        for nums, target in cases:
            print(nums, target, self.threeSumSmaller(nums, target))
            
            
            
# Solution().test()