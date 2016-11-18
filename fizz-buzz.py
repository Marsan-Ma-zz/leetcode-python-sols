# https://leetcode.com/problems/fizz-buzz/

# Write a program that outputs the string representation of numbers from 1 to n.

# But for multiples of three it should output “Fizz” instead of the number and 
# for the multiples of five output “Buzz”. For numbers which are multiples of 
# both three and five output “FizzBuzz”.


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        sol = []
        for i in range(1,n+1):
            if i % 15 == 0:
                sol.append('FizzBuzz')
            elif i % 5 == 0:
                sol.append('Buzz')
            elif i % 3 == 0:
                sol.append('Fizz')
            else:
                sol.append(str(i))
        return sol
    
                
    def test(self):
        print(self.fizzBuzz(20))
        
# Solution().test()