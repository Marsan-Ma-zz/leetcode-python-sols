# https://leetcode.com/problems/super-pow/

# Your task is to calculate ab mod 1337 where a is a positive integer and b 
# is an extremely large positive integer given in the form of an array.

# Example1:

# a = 2
# b = [3]

# Result: 8
# Example2:

# a = 2
# b = [1,0]

# Result: 1024



class Solution(object):

    # [CHEATING] actually python pow have build-in mod...
    def superPow(self, a, b):
        return pow(a, int(''.join(map(str, b))), 1337)


    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        
        def pow(a, b):
            # print(a, b)
            if b == 0:
                return 1
            elif b == 1:
                return a
            elif b % 2 == 1:
                return a*pow(a, b-1) % 1337
            else:
                return pow((a*a % 1337), b//2)
                
        # a**321 = ((a**3)**10 * a**2)**10 * a**1
        c = pow(a, b[0])
        for i in b[1:]:
            c = pow(c, 10) * pow(a, i) % 1337
        return c