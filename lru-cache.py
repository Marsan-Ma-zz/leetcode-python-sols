# https://leetcode.com/problems/lru-cache/

# Design and implement a data structure for Least Recently Used (LRU) cache. 
# It should support the following operations: get and set.

# get(key) - Get the value (will always be positive) of the key 
# if the key exists in the cache, otherwise return -1.

# set(key, value) - Set or insert the value if the key is not already 
# present. When the cache reached its capacity, it should invalidate the 
# least recently used item before inserting a new item.


import heapq

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.freq = []
        

    def get(self, key):
        """
        :rtype: int
        """
        res = self.cache.get(key)
        # print("get:", self.cache, self.freq)
        if res:
            self.freq.remove(key)
            self.freq += [key]
            return res
        else:
            return -1
        
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        # print("set_a:", self.cache, self.freq)
        res = self.cache.get(key)
        if res:
            self.freq.remove(key)
            self.freq += [key]
        elif len(self.cache) >= self.capacity:
            lru = self.freq[0]
            self.freq = self.freq[1:] + [key]
            del self.cache[lru]
        else:
            self.freq += [key]
        self.cache[key] = value
        # print("set_b:", self.cache, self.freq)
            
        
        