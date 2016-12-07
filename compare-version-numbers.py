# https://leetcode.com/problems/compare-version-numbers/

# Compare two version numbers version1 and version2.
# If version1 > version2 return 1, if version1 < version2 return -1, 
# otherwise return 0.

# You may assume that the version strings are non-empty and contain 
# only digits and the . character.
# The . character does not represent a decimal point and is used to 
# separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version 
# three", it is the fifth second-level revision of the second first-level 
# revision.

# Here is an example of version numbers ordering:

# 0.1 < 1.1 < 1.2 < 13.37


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        m1, m2 = version1.split('.'), version2.split('.')
        
        l1, l2 = len(m1), len(m2)
        if l1 > l2:
            m2.extend(['0']*(l1-l2))
        elif l2 > l1:
            m1.extend(['0']*(l2-l1))
        # print(m1, m2)
        
        for i, v in enumerate(m1):
            if int(v) > int(m2[i]):
                return 1
            elif int(v) < int(m2[i]):
                return -1
        return 0