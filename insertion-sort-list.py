# https://leetcode.com/problems/insertion-sort-list/

# Sort a linked list using insertion sort.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # [Ideas]
        # 1. insertion sort: compare from head to find insert point
        # 2. link-list is tricky, don't cause INF-LOOP!
        #    => use python one-line NON-BLOCKING ASSIGNMENT!!
        
        dummy = ListNode(-float('inf'))
        node = head
        while node:
            ptr, last = dummy, None
            while ptr and ptr.val < node.val:
                ptr, last = ptr.next, ptr
            if last: 
                last.next, node.next, node = node, ptr, node.next  # one-line NON-BLOCKING ASSIGNMENT!!
            else: # new head
                dummy.next, node.next, node = node, dummy.next, node.next # one-line NON-BLOCKING ASSIGNMENT!!
                
        return dummy.next
        