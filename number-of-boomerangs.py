# https://leetcode.com/problems/number-of-boomerangs/

# Given n points in the plane that are all pairwise distinct, 
# a "boomerang" is a tuple of points (i, j, k) such that the 
# distance between i and j equals the distance between i and k 
# (the order of the tuple matters).

# Find the number of boomerangs. You may assume that n will be at
# most 500 and coordinates of points are all in the range [-10000, 10000] 
# (inclusive).

# Example:
# Input:
# [[0,0],[1,0],[2,0]]

# Output:
# 2

# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]



from collections import defaultdict
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        # [Examples]
        # [[0,0],[1,0],[2,0]] => 2
        # => [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
        
        # [Ideas]
        # 1. is that possible to avoid calculate all pairs of distance?
        #    => seems no
        # 2. for each point as center, 
        #    use hashmap to save key:distance => value: pair
        #    then find common points
        # 3. to improve: no need to remember points, just increment count 
        #    for each center points, N wing points have N*N-1 permutations
        
        
        sols = 0
        for x1, y1 in points:
            dist = defaultdict(int)
            for x2, y2 in points:
                d = pow(x1-x2, 2) + pow(y1-y2, 2)
                dist[d] += 1
            for _, v in dist.items():
                sols += v*(v-1)
                        
        return sols
    
    
    def test(self):
        cases = [
            [],
            [[0,0]],
            [[0,0],[1,0]],
            [[0,0],[1,0],[2,0]],
            [[0,0],[1,0],[2,0],[3,0]],
            [[0,0],[1,0],[2,0],[3,0],[5,0]],
            [[0,0],[1,0],[0,1],[1,1]],
            [[0,0],[1,0],[0,1],[1,1],[0,2]],
            [[0,0],[1,0],[0,1],[1,1],[0,3]],
        ]
        for c in cases:
            print(c, self.numberOfBoomerangs(c))
                    
                
# Solution().test()