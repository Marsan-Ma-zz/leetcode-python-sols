# https://leetcode.com/problems/expression-add-operators/

# Given a string that contains only digits 0-9 and a target value, 
# return all possibilities to add binary operators (not unary) +, -, or * between 
# the digits so they evaluate to the target value.

# Examples: 
# "123", 6 -> ["1+2+3", "1*2*3"] 
# "232", 8 -> ["2*3+2", "2+3*2"]
# "105", 5 -> ["1*0+5","10-5"]
# "00", 0 -> ["0+0", "0-0", "0*0"]
# "3456237490", 9191 -> []



class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        
        # [Ideas]
        # 1. dfs, if meet *, reverse last calculation and combine with
        #    the * result.
        
        sols = []
        
        def dfs(val, s, rest, last):
            if not rest and val == target:
                sols.append(s)
                return
            for i in range(1, len(rest)+1):
                t, r = rest[:i], rest[i:]
                if rest[0] == '0' and i > 1:
                    continue
                if s == '':
                    dfs(val+int(t), t, r, int(t))
                else:
                    dfs(val+int(t), s+'+'+t, r,  int(t))
                    dfs(val-int(t), s+'-'+t, r, -int(t))
                    dfs(val-last+last*int(t), s+'*'+t, r, last*int(t))
        
        dfs(0, '', num, 0) 
        return sols
    
    
    def test(self):
        cases = [
            ('123', 6),
            ('232', 8),
            ('105', 5),
            ('00', 0),
            ('000', 0),
        ]
        for c, k in cases:
            print(c, k, self.addOperators(c, k))
            
            
# Solution().test()