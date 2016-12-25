# https://leetcode.com/problems/lexicographical-numbers/

# Given an integer n, return 1 - n in lexicographical order.

# For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

# Please optimize your algorithm to use less time and space. 
# The input size may be as large as 5,000,000.


class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        # [Ideas]
        # 1. use recursive? 
        #    1, (10,11...19), (100,(101,102...),(110,111,...)...)
        # 2. found rule!
        #    range(1, 2) + range(10, 20) + range(100, 200),
        #    range(2, 3) + range(20, 30) + range(200, 201), ...
        #    X. fk, it's wrong rule!
        # -----------------
        # 1. rule for "find next number": *10 or +1. 
        #    but if +1, kill tail trailing zeros after carry-in!
        #    23, 230, 2300(X) => 231, 2310(X) => 232 ... 239, 240(X) => 24
        
        sols = [1]
        while len(sols) < n:
            cur = sols[-1]*10
            while cur > n:
                cur = cur // 10 + 1
                while cur % 10 == 0:
                    cur = cur // 10
            sols.append(cur)
        return sols
    
    def test(self):
        cases = [
            # 0,
            # 8,
            # 18,
            # 38,
            200,
        ]
        for c in cases:
            print(c, self.lexicalOrder(c))
            
# Solution().test()