# https://leetcode.com/problems/different-ways-to-add-parentheses/

# Given a string of numbers and operators, return all possible results from 
# computing all the different possible ways to group numbers and operators. 
# The valid operators are +, - and *.


# Example 1
# Input: "2-1-1".

# ((2-1)-1) = 0
# (2-(1-1)) = 2
# Output: [0, 2]


# Example 2
# Input: "2*3-4*5"

# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
# Output: [-34, -14, -10, -10, 10]



class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        
        nums, j = [], 0
        input += ' ' # dummy for loop convenience
        
        for i in range(len(input)):
            if not input[i].isdigit():
                nums.append(input[j:i])
                j = i
        # print(nums)
        
        def helper(s):
            if not s: return [0]
            if len(s) == 1: return [int(s[0])]
            
            sols = []
            for i in range(1, len(s)):
                front, rear = s[:i], s[i:]
                sym = rear[0][0]
                rear[0] = rear[0][1:]
                grpa, grpb = helper(front), helper(rear)
                sols.extend(eval("%s%s%s" % (a, sym, b)) for a in grpa for b in grpb)
            return sols
        
        sols = helper(nums)
        # print(sols)
        return sols
        
                