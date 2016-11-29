# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

# Given a string, find the length of the longest substring T that 
# contains at most 2 distinct characters.

# For example, Given s = “eceba”,

# T is "ece" which its length is 3.


from collections import OrderedDict

class Solution(object):

    # [general solution for k-distinct-characters]
    # (https://discuss.leetcode.com/topic/37487/general-k-distinct-characters-solution-in-python)
    # The main idea is that using OrderedDict to save the last index current char appeared, 
    # and make the index in the OrderedDict ascendingly. When the length of OrderedDict is 
    # larger than K, move start to OrderedDict.first.val + 1 and remove OrderedDict.first.

    def lengthOfLongestSubstringTwoDistinct(self, s, k=2):
        queue, start, sol = OrderedDict(), 0, 0

        for i, char in enumerate(s):
            if char in queue:
                queue.pop(char)
            queue[char] = i

            if len(queue) > k:
                start = queue.popitem(False)[1] + 1
            sol = max(sol, i - start + 1)
        return sol



    # [Ideas]
    # eceba => ‘ece’ => 3
    # 1. one pass scan, memorize:
    #    a) char last appear place with hashmap
    #    b) latest 2 appeared char 
    # 2. current longest substring would be:
    #    a) composed by latest 2 apprar char “ca, cb”
    #    b) length = i - min(tbl[ca], tbl[cb])
    #    update best sol accordingly

    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # lat1 is latest                         # eceeceba
        lat1, lat2 = None, None                  # a  b  e  c
        pos1, pos2 = None, None                  # 7  6  5  1
        trans, best = 0, 0                       # 7, 2
        for i, c in enumerate(s):
            if c == lat1:
                pass
            elif c == lat2:
                lat1, lat2 = lat2, lat1
                pos1, pos2 = pos2, pos1
                trans = i 
            else:
                lat1, lat2 = c, lat1
                pos1, pos2 = i, trans
                trans = i
            if pos2 != None:
                # print(best, i, pos2)
                best = max(best, i - min(pos1, pos2) + 1)
        return best


    def test(self):
        cases = [
             '',
             'a',
             'ab',
             'aba',
             'eceba',
             'eceececba', 
        ]
        for c in cases:
            print(c, self.lengthOfLongestSubstringTwoDistinct(c))


# Solution().test()
