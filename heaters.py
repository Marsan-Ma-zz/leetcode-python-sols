# https://leetcode.com/problems/heaters/

# Winter is coming! Your first job during the contest is to design a standard heater 
# with fixed warm radius to warm all the houses.

# Now, you are given positions of houses and heaters on a horizontal line, find out minimum 
# radius of heaters so that all houses could be covered by those heaters.

# So, your input will be the positions of houses and heaters seperately, and your expected 
# output will be the minimum radius standard of heaters.

# Note:
# Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
# Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
# As long as a house is in the heaters' warm radius range, it can be warmed.
# All the heaters follow your radius standard and the warm radius will the same.

# Example 1:
# Input: [1,2,3],[2]
# Output: 1
# Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, 
# then all the houses can be warmed.

# Example 2:
# Input: [1,2,3,4],[1,4]
# Output: 1
# Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, 
# then all the houses can be warmed.



from collections import deque
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        
        # [Ideas]
        # 1. have to check all houses, at least O(n)
        # 2. "transfer points" are mid-points between continuous heater
        #    thus every house easily get it's own heater number
        # 3. scan houses and find house with farest distance with 
        #    belonged headter
        
        houses, heaters = sorted(houses), sorted(heaters)
        trans = deque([(i+j)/2 for i,j in zip(heaters, heaters[1:])])
        # print(houses, heaters)
        
        hidx = 0  # heater index
        sol = 0
        for h in houses:
            while trans and h > trans[0]:
                hidx += 1
                trans.popleft()
            sol = max(sol, abs(h-heaters[hidx]))
            # print(h, heaters[hidx])
        return sol
    
    
    def test(self):
        cases = [
            # ([], [3]),
            # ([4], [3]),
            # ([1,2,3], [2]),
            # ([1,2,3,4], [1,4]),
            # ([1,2,3,4,100], [1,4]),
            ([282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923],
[823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]),
        ]
        for hs, he in cases:
            print(hs, he, self.findRadius(hs, he))
            
            
# Solution().test()