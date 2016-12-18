# https://leetcode.com/problems/lfu-cache/

# Design and implement a data structure for Least Frequently Used (LFU) cache. 
# It should support the following operations: get and set.

# get(key) - Get the value (will always be positive) of the key if the key exists 
# in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present. 

# When the cache reaches its capacity, it should invalidate the least frequently used 
# item before inserting a new item. For the purpose of this problem, when there is a tie 
# (i.e., two or more keys that have the same frequency), the least recently used key 
# would be evicted.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LFUCache cache = new LFUCache( 2 /* capacity */ );

# cache.set(1, 1);
# cache.set(2, 2);
# cache.get(1);       // returns 1
# cache.set(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.get(3);       // returns 3.
# cache.set(4, 4);    // evicts key 1.
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4



from heapq import *

class LFUCache(object):
    
    # [Ideas]
    # 1. the frequency is dynamic, use hash or maybe heap?
    # 2. hash to save key-value, heap for finding least frequency to pop
    # 3. get => see hash content, update heap for frequency
    # 4. set => if capacity reached, pop LF from heap and delete from hash
    # 5. record frequency in heap, record recent use in ?
    #-------------------------
    # 6. TLE since there are a tricky algorithm dedicate for LFU cache.
    #    

    def __init__(self, capacity):
        """        
        :type capacity: int
        """
        self.tbl = {}   # (freq, timestamp, value)
        self.heap = []  # (freq, timestamp, key)
        self.capacity = capacity
        self.ts = 0 # timestamp, to solve "most recent" order

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        self.ts += 1
        
        # print(self.tbl, self.heap)
        freq, ts, sol = self.tbl.get(key, (None, None, -1))
        if sol == -1: return -1

        # update freq
        self.tbl[key] = (freq+1, self.ts, sol)
        idx = self.heap.index((freq, ts, key))
        self.heap[idx] = (freq+1, self.ts, key)
        heapify(self.heap)
        return sol


    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        self.ts += 1
        
        # update existing
        if key in self.tbl:
            freq, ts, _ = self.tbl[key]
            self.tbl[key] = (freq+1, self.ts, value)
            
            idx = self.heap.index((freq, ts, key))
            self.heap[idx] = (freq+1, self.ts, key)
            heapify(self.heap)
            return

        # insert new
        if self.capacity > 0:
            if len(self.tbl) >= self.capacity:
               _, _, pkey = heappop(self.heap)
               del self.tbl[pkey]
            self.tbl[key] = (1, self.ts, value)
            heappush(self.heap, (1, self.ts, key))




def test():
    obj = LFUCache(2)
    print(obj.get(3))
    obj.set(3,333)
    print(obj.get(3))
    obj.set(1,111)
    print(obj.get(3))
    obj.set(2,222)
    print(obj.get(3))
    obj.set(4,444)
    print(obj.get(3))
    print(obj.get(1))
    print(obj.get(2))

# test()
