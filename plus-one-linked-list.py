# https://leetcode.com/problems/plus-one-linked-list/

# Given a non-negative number represented as a singly linked list of digits, plus one to the number.

# The digits are stored such that the most significant digit is at the head of the list.

# Example:
# Input:
# 1->2->3

# Output:
# 1->2->4


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # [Ideas]
        # 1. the key is to make carry-in correct.
        # 2. reverse link-list, add-one, reverse again, cost O(3n)
        # 3. if we don't reverse, no good way to predict carry-in
        #----------------------------------
        # 1. actually we just need to find the latest number 
        #    which is not 9, the carry-in will stop at this node.
        # 2. after finding stopper, cases are:
        #    a) tail.val < 9, +1 and return
        #    b) tail.val == 9, start from stopper, +1 
        #       then all the next until tail set to 0
        #    c) stopper not found, all nodes are 9 =>
        #       add one more node '1' as new header,
        #       then set rest nodes to '0' 
        
        if not head: return
        
        # find carry-in stopper
        cur, stop = head, None
        while cur.next:
            if cur.val != 9:
                stop = cur
            cur = cur.next
        
        if cur.val < 9:
            cur.val += 1
        elif stop:
            stop.val += 1
            while stop.next:
                stop = stop.next
                stop.val = 0
        else:
            new_msb = ListNode(1)
            new_msb.next = head
            cur, head = head, new_msb
            while cur:
                cur.val = 0
                cur = cur.next
        return head
            
        
            
        