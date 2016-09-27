# https://leetcode.com/problems/summary-ranges/

# Given a sorted integer array without duplicates, return the summary of its ranges.

# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        if not nums: return []
        
        last = [nums[0], nums[0]]
        results = []
        
        # traverse
        for n in nums[1:]:
            if n == last[1]+1:
                last[1] = n
            else:
                if last[0] == last[1]:
                    results.append("%i" % (last[0]))
                else:
                    results.append("%i->%i" % (last[0], last[1]))
                last = [n, n]
            
        # finishing
        if last[0] == last[1]:
            results.append("%i" % (last[0]))
        else:
            results.append("%i->%i" % (last[0], last[1]))
            
        return results
    
    
    def test(self):
        cases = [
            [],
            [0,3,4,5,10,11],
            [0,1,2,4,5,7],
            [1,2],
            [10,11,15],
        ]
        for c in cases:
            res = self.summaryRanges(c)
            print(c, res)
            
# Solution().test()
