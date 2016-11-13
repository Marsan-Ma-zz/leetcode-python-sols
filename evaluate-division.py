# https://leetcode.com/problems/evaluate-division/

# Equations are given in the format A / B = k, 
# where A and B are variables represented as strings, 
# and k is a real number (floating point number). Given some queries, 
# return the answers. If the answer does not exist, return -1.0.

# Example:
# Given a / b = 2.0, b / c = 3.0. 
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].

# The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

# According to the example above:

# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
# The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.


from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        
        # [Example]
        # equations = [ ["a", "b"], ["b", "c"] ],
        # values = [2.0, 3.0],
        # queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
        
        # [Ideas]
        # 1. maybe could design as a graph? each edge used 1 at most
        #    a -> b, b -> c  / a -> c = a -> b -> c
        # 2. use a dict to describe this graph, dict value as edge weight
        # 3. no way to avoid this graph traversing, 
        #    sol is optimal as long as DFS is optimal
        # 4. since "no contradiction", we don't care it's shortest path
        #    as long as get 1 sol, it's correct sol 
        #    => thus DFS rather than BFS
        
        # build graph
        self.graph = defaultdict(dict)
        for (n1, n2), v in zip(equations, values):
            self.graph[n1][n2] = v
            self.graph[n2][n1] = 1/v
            
            
        # get answers
        sols = []
        for q1, q2 in queries:
            if (q1 not in self.graph) or (q2 not in self.graph):
                sols.append(-1.0)
            elif q1 == q2:
                sols.append(1.0)
            else:
                ans = self.dfs([q1], q2, 1)
                if ans == None: ans = -1
                sols.append(ans)
        return sols
    
    
    def dfs(self, seq, target, val):
        cur = seq[-1]
        cands = self.graph[cur]
        if target in cands:
            return val * cands[target]
        else:
            for q in cands:
                if q in seq: continue
                ans = self.dfs(seq+[q], target, val*cands[q])
                if ans: return ans
            return None
                    
            
    def test(self):
        eq  = [ ["a", "b"], ["b", "c"], ["c", "e"] ]
        val = [2.0, 3.0, 10.0]
        que = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
        sols = self.calcEquation(eq, val, que)
        return que, sols
        
        
que, sols = Solution().test()
for q, s in zip(que, sols):
    print(q, s)