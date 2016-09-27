# https://leetcode.com/problems/paint-fence/

# There is a fence with n posts, each post can be painted with one of the k colors.

# You have to paint all the posts such that no more than two adjacent fence posts have the same color.

# Return the total number of ways you can paint the fence.

# Note:
# n and k are non-negative integers.

class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
        # [Ideas]
        # 1. dynamic programming, sol[n] = sol[n-1] * k - k
        # 2. Ex: sol = [0, k, k*k, k*k*k - k, ...]
        
        if not n: return 0
            
        sols = [0, k, k**2]
        for i in range(3, n+1):
            # s = sols[-1]*k - k
            s = sum(sols[-2:])*(k-1)
            sols.append(s)
        return max(0, sols[n])