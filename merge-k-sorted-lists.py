# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


from heapq import *

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        # [Idea]
        # 1. it's a typical problem which heap suit the best
        # 2. because we have to maintain head of list sorted, 
        #    and this sort caction must be efficient for moving 1 item at a time.
        h = [(s.val, s) for s in lists if s]
        heapify(h)
        
        hnode = ListNode(-1)  # pseudo node
        hptr = hnode
        while h:
          v, s = heappop(h)
          hnode.next = ListNode(v)
          hnode = hnode.next
          if s.next:
            heappush(h, (s.next.val, s.next))
        return hptr.next
