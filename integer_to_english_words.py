# Convert a non-negative integer to its english words representation. 
# Given input is guaranteed to be less than 2^31 - 1.

# For example,
# 123 -> "One Hundred Twenty Three"
# 12345 -> "Twelve Thousand Three Hundred Forty Five"
# 1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

class Solution(object):
    mapper = {
      # 0: 'zero',
      1: 'one',
      2: 'two',
      3: 'three',
      4: 'four',
      5: 'five',
      6: 'six',
      7: 'seven',
      8: 'eight',
      9: 'nine',
      10: 'ten',
      #----------
      11: 'eleven',
      12: 'twelve',
      13: 'thirteen',
      14: 'fourteen',
      15: 'fifteen',
      16: 'sixteen',
      17: 'seventeen',
      18: 'eighteen',
      19: 'nineteen',
      #----------
      20: 'twenty',
      30: 'thirty',
      40: 'forty',
      50: 'fifty',
      60: 'sixty',
      70: 'seventy',
      80: 'eighty',
      90: 'ninety',
    }

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        # [Ideas]
        # 1. 2^31 -1 => smaller than 4 billion (4 * 1024^3)
        # 2. 3 digits per group: ('' => thousands => million => billion)
        # 3. helper function process one single group (smaller than 1000)
        # 4. concat from MSB group to LSB group
        # 5. Ex: 1234567 => (1) million (234) thousands and (567)
        # -----------------------
        # 6. each group: x hundred (if > 100) 
        if not num: return 'Zero'
        # print(num)
        grp_0 = num // 1e9
        grp_1 = (num // 1e6) % 1e3
        grp_2 = (num // 1e3) % 1e3
        grp_3 = num % 1e3

        res = []
        if grp_0:
            res += self.process_grp(grp_0) + ['billion']
        if grp_1:
            res += self.process_grp(grp_1) + ['million']
        if grp_2:
            res += self.process_grp(grp_2) + ['thousand']
        if grp_3:
            res += self.process_grp(grp_3)
        res = [w.capitalize() for w in res]
        return  ' '.join(res)

    
    def process_grp(self, num):
        res = []
        # print("num", num)
        if num // 100:
            res += [self.mapper[num // 100], 'hundred']
        num = num % 100
        if (num in self.mapper):
            res += [self.mapper[num]]
            return res
        elif num == 0:
            return res  # zero not dealing here, as exception in the begin
        else :
            res += [self.mapper[num - (num % 10)]]
            res += [self.mapper[num % 10]]
            return res
        
    def test(self):
        cases = [
            None,
            0,
            1,
            9,
            10,
            15,
            20,
            40,
            80,
            100,
            101,
            123,
            1000,
            1001,
            1234,
            12345,
            123456,
            1234567,
        ]
        for c in cases:
            print(c, self.numberToWords(c))
            
            
Solution().test()