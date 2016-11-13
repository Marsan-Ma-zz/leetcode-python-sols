# https://leetcode.com/problems/missing-ranges/

# Given a sorted integer array where the range of elements 
# are [lower, upper] inclusive, return its missing ranges.

# For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, 
# return ["2", "4->49", "51->74", "76->99"].



class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        
        last = lower
        results = []
        
        # traverse
        for n in nums:
            if n < lower: 
                continue
            elif n > upper:
                break 
            elif n == last+1:
                results.append("%s" % last)
            elif n > last+1:
                results.append("%s->%s" % (last, n-1))
            last = n+1
            
        # finishing
        if last == upper:
            results.append("%s" % upper)
        elif last < upper:
            results.append("%s->%s" % (last, upper))
            
        return results
    
    
    def test(self):
        cases = [
            ([], 0, 100),
            ([1], 0, 100),
            ([10, 20,21, 50,51,52,53,54], 0, 100),
            ([0, 1, 3, 50, 75], 0, 99),
        ]
        for nums, lower, upper in cases:
            res = self.findMissingRanges(nums, lower, upper)
            print(nums, lower, upper, res)

            
# Solution().test()

# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")

