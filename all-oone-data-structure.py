# https://leetcode.com/problems/all-oone-data-structure/

# Implement a data structure supporting the following operations:

# Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. 
# Key is guaranteed to be a non-empty string.

# Dec(Key) - If Key's value is 1, remove it from the data structure. 
# Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. 
# Key is guaranteed to be a non-empty string.

# GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
# GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
# Challenge: Perform all these in O(1) time complexity.



class Node(object):
    def __init__(self, val):
        self.sets = set([])
        self.nxt = None
        self.lst = None
        self.val = val


class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = {}
        self.head, self.tail = Node(0), Node(-1) # dummy min, dummy max
        self.head.nxt, self.tail.lst = self.tail, self.head
        self.vals = {0: self.head, -1: self.tail}  # pointer to link list

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        val = self.keys.get(key, 0)
        self.keys[key] = val+1
        
        # add new node
        if val+1 not in self.vals:
            last, node = self.tail.lst, Node(val+1)
            last.nxt = node
            self.tail.lst = node
            node.nxt, node.lst = self.tail, last
            self.vals[val+1] = node
        
        if key in self.vals[val].sets:
            self.vals[val].sets.remove(key)
        self.vals[val+1].sets.add(key)
            

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.keys:
            val = self.keys[key]
            self.vals[val].sets.remove(key)
            if val == 1:
                del self.keys[key]
            else:
                self.keys[key] = val - 1
                self.vals[val-1].sets.add(key)

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        # for k, v in self.vals.items():
        #     print(k, v.val, v.sets)
        node = self.tail.lst
        while node and not node.sets:
            node = node.lst
        return list(node.sets)[0] if node else ''
        

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        node = self.head.nxt
        while node and not node.sets:
            node = node.nxt
        return list(node.sets)[0] if node else ''


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()