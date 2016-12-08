# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

# Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.
# Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

# Could you do this in O(n) runtime?

# Example:
# Input: [3, 10, 5, 25, 2, 8]
# Output: 28
# Explanation: The maximum result is 5 ^ 25 = 28.


class Solution(object):
    
    # [Ideas]
    # 1. compare 1 string with "all the others" at a time => use Trie!
    # 2. one bit in MSB is better than all the rest bits in LSB
    #    => check from MSB to LSB, always choose path making current bit xor = 1
    # 3. trick: use 1^c instead of int(not c)
    
    def findMaximumXOR(self, nums):
        
        # build trie
        root = {}
        for n in nums:
            node = root
            for i in reversed(range(32)):
                c = (n >> i) & 1
                node = node.setdefault(c, {})
        # print(root)
        
        # scan for nums
        best = 0
        for n in nums:
            node = root
            xor = 0
            for i in reversed(range(32)):
                c = (n >> i) & 1
                if 1^c in node:
                    node = node[1^c]
                    xor += (1 << i)
                elif c in node:
                    node = node[c]
            best = max(best, xor)
        return best
        
        
    
    def test(self):
        cases = [
            [3, 10, 5, 25, 2, 8],
            # [11, 1010, 101, 11001, 10, 1000]
        ]
        for c in cases:
            print(c, self.findMaximumXOR(c))
            
            
# Solution().test()
