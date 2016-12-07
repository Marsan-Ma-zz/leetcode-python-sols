# https://leetcode.com/problems/remove-linked-list-elements/

# Remove all elements from a linked list of integers that have value val.

# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # get valid head
        while head:
            if head.val == val:
                head = head.next
            else:
                break
        if not head: return None
        
        # clear rest linklist
        node, last = head.next, head
        while node:
            if node.val == val:
                last.next = node.next
            else:
                last = node
            node = node.next
        return head
        