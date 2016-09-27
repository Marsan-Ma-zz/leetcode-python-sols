class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        
        # [Ideas]
        # 1. parse 1 number and check following accordingly
        #    once violate, return False
        # 2. if data consumed completely without violation, return True
        
        if not data: return True
        
        i = 0
        while i < len(data):
            if data[i] < 128:
                i += 1
                continue        # single byte, always valid
            elif 192 <= data[i] < 255:
                bcnt = self.byte_num(data[i])
                if i + bcnt > len(data):
                    return False
                for k in range(1, bcnt):
                    if data[i+k] >> 6 != 2:
                        return False
                i += bcnt
            else:  # data[i] == 255 or 128 <= data[i] < 192
                return False
        return True
                
            
    # only deal 192 <= word < 255        
    def byte_num(self, word):    
        level = 7
        cnt = 0
        while True:
            if (word >> level) % 2 == 1:
                cnt += 1
                level -= 1
            else:
                break
        # print("byte:", cnt)
        return cnt
            
            
    def test(self):
        cases = [
            [],
            [197, 130, 1],
            [235, 140, 4],
            [197, 130, 1, 7, 16],
            [235, 140, 135, 4, 7, 197, 130, 1, 7, 16],
            [255],
        ]
        for c in cases:
            print(c, self.validUtf8(c))
            
            

Solution().test()