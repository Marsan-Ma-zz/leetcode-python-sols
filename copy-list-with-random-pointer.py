# https://leetcode.com/problems/copy-list-with-random-pointer/

# A linked list is given such that each node contains an additional 
# random pointer which could point to any node in the list or null.

# Return a deep copy of the list.


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        # [Ideas]
        # 1. key: how to link to node haven't created?
        #         how to link to previous created nodes?
        # 2. each time create current node and 1 or 2 next node,
        #    record unfinished node in queue? hash? 
        # 3. if use hash, what's the id? use original copy as id?
        
        tbl = {}
        node = head
        head_copy = None
        
        def get_or_create(m):
            if m not in tbl:
                tbl[m] = RandomListNode(m.label)
            return tbl[m]
            
        while node:
            n = get_or_create(node)
            if node.next:
                n.next = get_or_create(node.next)
            if node.random:
                n.random = get_or_create(node.random)
            if not head_copy:
                head_copy = n
            node = node.next
            
        return head_copy
        