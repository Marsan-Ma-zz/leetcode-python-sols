# https://leetcode.com/problems/strobogrammatic-number/

# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

# Write a function to determine if a number is strobogrammatic. The number is represented as a string.

# For example, the numbers "69", "88", and "818" are all strobogrammatic.


class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        
        if not num: return True
        
        for n in num:
            if n not in ['0','1','6','8','9']:
                return False
                
        l = len(num)
        
        if (l % 2 == 1) and (num[l//2] not in ['0', '1', '8']):
            return False
        
        p1, p2 = 0, len(num)
        for i in range(l//2):
            if (num[i] in ['0', '1', '8']) and (num[l-1-i] != num[i]):
                return False
            if (num[i] == '6') and (num[l-1-i] != '9'):
                return False
            if (num[i] == '9') and (num[l-1-i] != '6'):
                return False
        return True
        
        
    def test(self):
        cases = [
            "",
            "11",
            "181",
            "1881",
            "5",
            "16891",
            "166891",
        ]
        for c in cases:
            print(c, self.isStrobogrammatic(c))
            
            
# Solution().test()            