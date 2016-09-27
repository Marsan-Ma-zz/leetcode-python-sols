from math import ceil, floor

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        # [Ideas]
        # 1. candidates: [0, 1, 6, 8, 9]
        # 2. special: 0 can't be start or end
        # 3. we only need to construct the first ceil(n/2) digits,
        #    and 1st digit can't be '0'
        
        if not n: return []
        
        
        mid_cands = ['0', '1', '8']
        cands = ['0','1','6','8','9']
        mapper = {'0': '0', '1':'1', '6':'9', '8':'8', '9':'6'}
        sols = ['1','6','8','9']    # 1st digit
        
        if n == 1: return mid_cands
        
        # generate half-sols
        for _ in range(1, int(floor(n/2))):
            sols = [[sol + ca for ca in cands] for sol in sols]
            sols = [j for k in sols for j in k] # flatten
        # print(sols)
        
        
        # middle digit
        if n % 2 == 1:
            sols = [[sol + ca for ca in mid_cands] for sol in sols]
            sols = [j for k in sols for j in k] # flatten
        
        # complete sols
        for i in range(len(sols)):
            rest = [mapper[k] for k in sols[i][:n//2][::-1]]
            sols[i] = sols[i] + ''.join(rest)
        # print(sols)
                
        return sols


    def test(self):
        cases = [
            0, 1, 2, 3,
        ]
        for c in cases:
            print(c, self.findStrobogrammatic(c))
            
# Solution().test()
