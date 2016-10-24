# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Given a linked list, remove the nth node from the end of list and return its head.

# For example,

#    Given linked list: 1->2->3->4->5, and n = 2.

#    After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        # [Ideas]
        # 1. use two pointer, 1 leading n node
        # 2. while leading node at tail, cut slower node.
        
        # boundary case
        if not head.next:
            return None # only one node, and remove it
        
        # initialize
        lead, lag, last = head, head, head
        for _ in range(n):
            lead = lead.next
            
        if lead:
            lead, lag = lead.next, lag.next
        else:  # only if we are removing the head
            return head.next
            
        # normal case: cut and connect
        while lead:
            lead, lag, last = lead.next, lag.next, last.next
            
        last.next = lag.next
        
        return head