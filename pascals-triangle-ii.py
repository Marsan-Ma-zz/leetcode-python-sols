# https://leetcode.com/problems/pascals-triangle-ii/

# Given an index k, return the kth row of the Pascal's triangle.

# For example, given k = 3,
# Return [1,3,3,1].

# Note:
# Could you optimize your algorithm to use only O(k) extra space?



class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # Ex:
        #  1 3 3 1 0
        #    1 3 3 1
        #------------
        #  1 4 6 4 1
        
        a = [1]
        for i in range(rowIndex):
            a.append(0)
            tmp = a[0]
            for j in range(1, len(a)):
                a[j], tmp = a[j]+tmp, a[j]
        return a
        
        