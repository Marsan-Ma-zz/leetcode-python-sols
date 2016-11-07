# https://leetcode.com/problems/text-justification/

# Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left justified and no extra space is inserted between words.

# For example,
# words: ["This", "is", "an", "example", "of", "text", "justification."]
# L: 16.



class Solution(object):
    def fullJustify(self, words, maxWidth=16):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        
        # [Ideas]
        # 1. dispatch words into lines, then handle one line at a time.
        
        # dispatch to lines
        cnt, grp, grps = 0, [], []
        for w in words:
            # if not w: continue
            cnt += (len(w) if cnt == 0 else len(w) + 1)
            if cnt <= maxWidth:
                grp.append(w)
            else:
                grps.append(grp)
                cnt, grp = len(w), [w]
        if grp: grps.append(grp)    # last line
        # print(grps)
            
        # handle lines
        lines = [self.gen_line(line, maxWidth) for line in grps[:-1]]
        
        # special: last line
        last_line = ' '.join(grps[-1])
        last_line += ' ' * (maxWidth - len(last_line))
        lines.append(last_line)
        
        return lines
            
        
    def gen_line(self, line, wmax):
        scnt = max(1, len(line)-1)  # space count
        base_len = sum([len(w) for w in line]) + scnt
        rest = wmax - base_len
        
        spaces = [' ' * (rest // scnt + 1)] * scnt
        for i in range(rest % scnt):
            spaces[i] += ' '
        # print(spaces)
        
        res = ''
        for i in range(scnt):
            res += line[i] + spaces[i]
        if len(line) > 1: res += line[-1]
        return res
        
        
    def test(self):
        cases = [
            ([''], 0),
            ([''], 5),
            (['abcde', 'abcde'], 5),
            (['abcde', 'abcde', 'abcde', 'abc', 'abcde'], 5),
            (['abcde', 'abcde', 'abcde', 'abc', 'abcde'], 6),
            
            ([''], 16),
            (['abc'], 16),
            (['abcdeabcdeabcdea'], 16),
            (['abcdeabcdeabcd.'], 16),
            (['abcde', 'abcde'], 16),
            (['abcde', 'abcde', 'abcde'], 16),
            (['abcde', 'abcde', 'abcde', 'abcde', 'abcde'], 16),
            (['abcde', 'abcde', 'abcde', 'abc', 'abcde'], 16),
            (['abcde', 'abcde', 'abcde', 'abc', 'ab.'], 16),
            (["This", "is", "an", "example", "of", "text", "justification."], 16),
        ]
        for c, mw in cases:
            # print(c)
            print(self.fullJustify(c, mw))
            
            
# Solution().test()
# print(10 % 3 + 2)