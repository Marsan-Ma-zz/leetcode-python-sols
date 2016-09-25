# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...

# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.

# Note: The sequence of integers will be represented as a string.

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        # [Ideas]
        # 1. the only way might be start from 1, and count up.
        
        if not n: return ''

        results = {
          1: '1'
        }
        for i in range(2, n+1):
            s_last, s_cur = results[i-1], ''
            label, cnt = None, 0
            for c in s_last:
                if (c != label):
                    if label: s_cur += "%i%s" % (cnt, label)
                    label, cnt = c, 1
                else:
                    cnt += 1
            s_cur += "%i%s" % (cnt, label)
            results[i] = s_cur
            # print(results)
        return results[n]

    def test(self):
        cases = [0, 1, 2, 3, 4, 5, 6, 7]
        for c in cases:
            print(c, self.countAndSay(c))


Solution().test()