# https://leetcode.com/problems/palindrome-linked-list/

# Given a singly linked list, determine if it is a palindrome.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        # [Ideas]
        # 1. 1st round find middle point
        # 2. 2nd round: before middle => push values into stack  
        #               after middle => pop values and verify equal
        # X, this will use O(n/2) space
        #---------------
        # [for O(1) space]
        # 1. 1st round still find middle point
        # 2. 2nd round break link in middle then reverse right half
        # 3. 3rd round check both half list are euqal
        
        if not head: return True
        
        # 1st round:
        length = 0
        current = head
        while current:
            current = current.next
            length += 1
            
        # 2nd round
        half = length // 2
        current = head
        for i in range(half):
            current = current.next
            
        # skip middle point if length is odd
        if length % 2: 
            current = current.next
            
        # reverse right half
        last = None
        for i in range(half):
            # update link
            next_node, current.next = current.next, last
            # update node
            last, current = current, next_node
        new_head = last
        
        # 3rd round
        current_1 = head
        current_2 = new_head
        for i in range(half):
            # print(current_1, current_2)
            if (current_1.val != current_2.val):
                return False
            current_1 = current_1.next
            current_2 = current_2.next
        return True
        