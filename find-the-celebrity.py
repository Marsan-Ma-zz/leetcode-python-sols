# https://leetcode.com/problems/find-the-celebrity/

# Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

# Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

# You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.

# Note: There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

# Show Company Tags
# Show Tags


# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # [Idea]
        # 1. everyone in a line, start from person 0 to n
        # 2. current = A, ask A -> B, if A knows B then A not celebrity (current = B), 
        #                             if not, B not celebrity (current = A)
        # 3. while we arrive celebrity (N) and current = celebrity, he don't know all the rest people.
        # 4. finally, we ask whether he (N) knows people from 0 to N-1, to verify he knows nobody.
        # 5. again we ask everyone to know him (N) to make sure he is famous.
        if n == 0: return None
        if n == 1: return 1
            
        cur = 0
        # find someone knows nobody
        for t in range(1, n):
            if knows(cur, t):
                cur = t
        for i in range(cur):
            if knows(cur, i):
                return -1
                
        # verify everyone knows him
        for i in range(n):
            if not knows(i, cur):
                return -1
        return cur
        
        
        