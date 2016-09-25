# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # [Idea]
        # 1. iterate through whole list, reverse it.
        
        if not head:
            return None
        
        # reverse link-list
        last_node = None
        next_node = None
        while head.next:
            next_node = head.next
            head.next = last_node
            last_node = head
            head = next_node
            
        # last node
        head.next = last_node
        return head
        
        