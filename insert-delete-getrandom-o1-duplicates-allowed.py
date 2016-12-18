# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

# Design a data structure that supports all following operations in average O(1) time.

# Note: Duplicate elements are allowed.
# insert(val): Inserts an item val to the collection.
# remove(val): Removes an item val from the collection if present.
# getRandom: Returns a random element from current collection of elements. 
# The probability of each element being returned is linearly related to the number of same 
# value the collection contains.

# Example:

# // Init an empty collection.
# RandomizedCollection collection = new RandomizedCollection();

# // Inserts 1 to the collection. Returns true as the collection did not contain 1.
# collection.insert(1);

# // Inserts another 1 to the collection. Returns false as the collection contained 1. 
# Collection now contains [1,1].

# collection.insert(1);

# // Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
# collection.insert(2);

# // getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
# collection.getRandom();

# // Removes 1 from the collection, returns true. Collection now contains [1,2].
# collection.remove(1);

# // getRandom should return 1 and 2 both equally likely.
# collection.getRandom();



from random import choice
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.idxs = {}

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.nums.append(val)
        s = self.idxs.get(val)
        if not s:
            self.idxs[val] = {len(self.nums)-1}
        else:
            self.idxs[val].add(len(self.nums)-1)
        return s == None

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        s = self.idxs.get(val)
        if not s: return False
        
        # pop target value
        # print(val, self.idxs, self.nums)    # (30, {10: [], 20: [2, 0], 30: [4]}, [20, 30, 20])
        idx = self.idxs[val].pop()
        self.nums[idx] = self.nums[-1]
        
        # fix moved value
        tail = len(self.nums)-1
        if idx != tail:
            val = self.nums[idx]
            self.idxs[val].remove(tail)
            self.idxs[val].add(idx)
        self.nums.pop()
        return True
        
        
    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return choice(self.nums)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()