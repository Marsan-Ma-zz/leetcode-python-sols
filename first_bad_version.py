# You are a product manager and currently leading a team to develop a new product. 
# Unfortunately, the latest version of your product fails the quality check. 
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
# which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which will return whether version is bad. 
# Implement a function to find the first bad version. You should minimize the number of calls to the API.

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n: return
    
        ptr1, ptr2 = 1, n                   # 1, 2
        while ptr1+1 < ptr2:                    
            ptr = (ptr1 + ptr2) // 2
            if isBadVersion(ptr):
                ptr2 = ptr
            else:
                ptr1 = ptr
        
        res = ptr1 if isBadVersion(ptr1) else ptr2
        return res
            
        