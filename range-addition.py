# https://leetcode.com/problems/range-addition/

# Assume you have an array of length n initialized with all 0's 
# and are given k update operations.

# Each operation is represented as a triplet: [startIndex, endIndex, inc] 
# which increments each element of subarray A[startIndex ... endIndex] 
# (startIndex and endIndex inclusive) with inc.

# Return the modified array after all k operations were executed.

# Example:
# Given:
#     length = 5,
#     updates = [
#         [1,  3,  2],
#         [2,  4,  3],
#         [0,  2, -2]
#     ]

# Output:

#     [-2, 0, 3, 5, 3]
# Explanation:

# Initial state:
# [ 0, 0, 0, 0, 0 ]

# After applying operation [1, 3, 2]:
# [ 0, 2, 2, 2, 0 ]

# After applying operation [2, 4, 3]:
# [ 0, 2, 5, 5, 3 ]

# After applying operation [0, 2, -2]:
# [-2, 0, 3, 5, 3 ]


class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        
        # [Ideas]
        # 1. record all updates as "delta value start from this position"
        # 2. after k updates, traverse through all n items with a level
        #    keep pick up delta values and update value for current position
        
        items = [0] * length
        for start, end, delta in updates:
            start = max(0, start)
            items[start] += delta
            if end < length-1:
                items[end+1] -= delta
            # print(items)
            
        level = 0
        for i in range(length):
            level += items[i]
            items[i] = level
            
        return items
    
    
    def test(self):
        updates = [
            [1,  3,  2],
            [2,  4,  3],
            [0,  2, -2],
            [-2, 2, 10],
            [1, 10, 100],
        ]
        ans = self.getModifiedArray(5, updates)
        print(ans)
            
        
# Solution().test()