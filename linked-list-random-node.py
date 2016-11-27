# https://leetcode.com/problems/linked-list-random-node/

# Given a singly linked list, return a random node's value from the linked 
# list. Each node must have the same probability of being chosen.

# Follow up:
# What if the linked list is extremely large and its length is unknown to 
# you? Could you solve this efficiently without using extra space?

# Example:

# // Init a singly linked list [1,2,3].
# ListNode head = new ListNode(1);
# head.next = new ListNode(2);
# head.next.next = new ListNode(3);
# Solution solution = new Solution(head);

# // getRandom() should return either 1, 2, or 3 randomly. Each element 
# should have equal probability of returning.
# solution.getRandom();



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


from random import random
class Solution(object):


    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head        
        


    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        node = self.head
        i, v = 1, node.val
        while node:
            if i * random() < 1:
                v = node.val
            node = node.next
            i += 1
        return v




# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


