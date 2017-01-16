# https://leetcode.com/problems/combination-sum-iii/

# Find all possible combinations of k numbers that add up to a number n, 
# given that only numbers from 1 to 9 can be used and each combination should be 
# a unique set of numbers.


# Example 1:

# Input: k = 3, n = 7

# Output:

# [[1,2,4]]

# Example 2:

# Input: k = 3, n = 9

# Output:

# [[1,2,6], [1,3,5], [2,3,4]]



class Solution(object):
    results = None
    n = None
    
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        
        1. comb(k, n, []) => comb(k-1, i, [j])
        """
        self.n = n
        self.results = []
        self.comb(k, 9, [])
        return self.results
        
    def comb(self, k, m, sol):
        sum_sol = sum(sol)
        if (k > 0) & (m > 0):
            v_max = min(self.n-sum_sol, m)
            for i in range(1,v_max+1):
                self.comb(k-1, i-1, sol + [i])
        elif (k == 0):
            if (sum_sol == self.n):
                sol.reverse()
                self.results.append(sol)
            print(sum_sol, sol, k)
                