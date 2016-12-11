# https://leetcode.com/problems/palindrome-partitioning-ii/

# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return the minimum cuts needed for a palindrome partitioning of s.

# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.



from collections import deque
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # [Ideas]
        # 1. BFS, cut first palindrome, then 2nd, then 3rd
        #    if cut done, it's the sol
        
        
        step = 0
        q = deque([s])
        visited = set()
        while q:
            step += 1
            for i in range(len(q)):
                c = q.popleft()
                for i in reversed(range(1, len(c)+1)):
                    cur, rest = c[:i], c[i:]
                    # bfs if cur is palindrome
                    if cur == cur[::-1]:
                        if not rest: return step-1 # cut=step-1
                        # cut tried
                        if len(rest) in visited: 
                            continue
                        else:
                            visited.add(len(rest))
                            q.append(rest)
                            print(cur, rest)
        return -1
    
    def test(self):
        cases = [
            # "",
            # "abc",
            "aab",
            # "abb",
            # "fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi",
        ]
        for c in cases:
            print(c, self.minCut(c))
            
# Solution().test()