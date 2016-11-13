# https://leetcode.com/problems/h-index-ii/

# Follow up for H-Index: What if the citations array is sorted 
# in ascending order? Could you optimize your algorithm?

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        idx      =>  0,1,2,3,4,5,6,7,8,9,10
        citations = [0,0,1,2,3,4,4,4,6,9,12]
        l-idx    => 10,9,8,7,6,5,4,3,2,1,0
                                 ^ans
        1. binary-search for citations[idx] > (l-idx) barely, in O(log(n))
        """
        cite_len = len(citations)
        if cite_len == 0: return 0
        
        # binary search
        lp, rp = 0, cite_len-1
        hidx = 0
        while True:
            ptr = lp + (rp-lp) // 2
            if citations[ptr] >= (cite_len - ptr):
                rp = ptr - 1
            elif citations[ptr] < (cite_len - ptr):
                lp = ptr + 1
            if rp < lp:
                hidx = (cite_len - lp)
                break
        return hidx
        