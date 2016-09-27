# https://leetcode.com/problems/reconstruct-itinerary/

# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

# Note:
# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# Example 1:
# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
# Example 2:
# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
# Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.


from collections import defaultdict

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        
        # [Ideas]
        # 1. construct mapper using hash
        # 2. use recursive to do DFS, smaller lexical order first
        # 3. if all trips used, that's correct answer.
        
        if not tickets: return []
        
        self.trips = defaultdict(dict)
        for k,v in tickets:
            if v in self.trips[k]: 
                self.trips[k][v] += 1
            else:
                self.trips[k][v] = 1
                
        ans = self.dfs([('', 'JFK')], len(tickets))
        ans = [d for _, d in ans]
        return ans
        
        
    def dfs(self, journey, rest):
        if rest == 0:
            return journey
        else:
            cur = journey[-1][1]
            for p in sorted(self.trips[cur]):
                if journey.count((cur, p)) < self.trips[cur][p]:
                    ans = self.dfs(journey + [(cur, p)], rest-1)
                    if ans: return ans
            return []
        
        
    
    def test(self):
        cases = [
            [],
            [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]],
            [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
            [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]],
            [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]],
        ]
        for c in cases:
            print(self.findItinerary(c))
    
    
    
# Solution().test()