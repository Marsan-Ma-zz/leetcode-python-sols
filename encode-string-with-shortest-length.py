# https://leetcode.com/problems/encode-string-with-shortest-length/

# Given a non-empty string, encode the string such that its encoded length 
# is the shortest.

# The encoding rule is: k[encoded_string], where the encoded_string inside 
# the square brackets is being repeated exactly k times.

# Note:
# k will be a positive integer and encoded string will not be empty or have 
# extra space.
# You may assume that the input string contains only lowercase English letters. 
# The string's length is at most 160.
# If an encoding process does not make the string shorter, then do not encode it. 
# If there are several solutions, return any of them is fine.

# Example 1:

# Input: "aaa"
# Output: "aaa"
# Explanation: There is no way to encode it such that it is shorter than the input string, 
# so we do not encode it.

# Example 2:

# Input: "aaaaa"
# Output: "5[a]"
# Explanation: "5[a]" is shorter than "aaaaa" by 1 character.
# Example 3:

# Input: "aaaaaaaaaa"
# Output: "10[a]"
# Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have the same 
# length = 5, which is the same as "10[a]".

# Example 4:

# Input: "aabcaabcd"
# Output: "2[aabc]d"
# Explanation: "aabc" occurs twice, so one answer can be "2[aabc]d".
# Example 5:

# Input: "abbbabbbcabbbabbbc"
# Output: "2[2[abbb]c]"
# Explanation: "abbbabbbc" occurs twice, but "abbbabbbc" can also be encoded to "2[abbb]c", 
# so one answer can be "2[2[abbb]c]".




class Solution(object):
    
    
    # from: https://discuss.leetcode.com/topic/71442/short-python
    # Either don't encode s at all, or encode it as one part k[...] or encode it as multiple parts 
    # (in which case we can somewhere split it into two subproblems). Whatever is shortest. 
    # Uses @rsrs3's nice trick of searching s in s + s.
    def encode(self, s, memo={}):
        if s not in memo:
            n = len(s)
            i = (s + s).find(s, 1)
            one = '%d[%s]' % (n / i, self.encode(s[:i])) if i < n else s
            multi = [self.encode(s[:i]) + self.encode(s[i:]) for i in xrange(1, n)]
            memo[s] = min([s, one] + multi, key=len)
        return memo[s]


    def encode(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # [Ideas]
        # 1. dfs, split into two part, if first part could compress, then try 2nd.
        # 2. TLE 33/34 ...

        dp = {}
        
        def dfs(s):
            if s not in dp:
                best = s
                for i in range(len(s)):
                    for j in reversed(range(i+1, len(s))):
                        
                        # check compressable
                        cnt, step = 1, len(s[i:j])
                        while s[i:j] == s[i+step*cnt:j+step*cnt]:
                            cnt += 1
                            comp = "%i[%s]" % (cnt, dfs(s[i:j]))
                            if len(comp) >= cnt*step: continue
                            # check better sol
                            sol = s[:i]+comp + dfs(s[i+step*cnt:])
                            if len(sol) < len(best): 
                                best = sol
                dp[s] = best
            return dp[s]
        
        sol = dfs(s)
        # for k,v in dp.items(): print(k,v)
        return sol
                            
                    
    def test(self):
        cases = [
            "",
            "aaa",
            "aaaaaaaaaa",
            "aabcaabcd",
            "abbbabbbcabbbabbbc",
            "aaaaaaaaaabbbaaaaabbb",    # "5[a]2[5[a]bbb]"
            "abcdcdcdabcdcdcdxyxyxyxy",
        ]
        for c in cases:
            print(self.encode(c))
            
# Solution().test()