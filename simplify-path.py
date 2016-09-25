# https://leetcode.com/problems/simplify-path/

# Given an absolute path for a file (Unix-style), simplify it.

# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        # [Idea]
        # 1. split by '/' => cases 
        #                    1) '.' skip
        #                    2) '..' pop 1 from stack
        #                    3) others, push to stack
        
        if not path: return None
        
        fpath = []
        for i in path.split('/'):
            if (i == '.') or (i == ''):
                pass
            elif i == '..':
                if fpath: fpath.pop()
            else:
                fpath.append(i)
        res = '/' + '/'.join(fpath)
        return res
    
    def test(self):
        cases = [
            '',
            '/',
            '../',
            'a/b/../c',
            'a/b/../../../c/d',
            'a/b/k/../../../c/d',
            '/a/b/../c',
            '/a/b/../../../c/d',
            '/a/b/k/../../../c/d',
        ]
        for c in cases:
            res = self.simplifyPath(c)
            print(res)
            
            
# Solution().test()