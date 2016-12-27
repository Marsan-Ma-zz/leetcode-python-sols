# https://leetcode.com/problems/linked-list-cycle-ii/

# Given a linked list, return the node where the cycle begins. 
# If there is no cycle, return null.

# Note: Do not modify the linked list.



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # [Ideas]
        # 1. fast/slow pointer meet at *:
        #    => 2*(a + b) = a + b + c + b
        #    => 2a + 2b = a + 2b + c
        #    => a = c
        # 2. after meet, 2 slower start from @ and *,
        #    their meet would be start of loop!
        #              c
        #            +--------*-----+
        #            |              | b
        #   @--------v--------------+
        #      a                  
        #
        
        fast, slow, slow2 = head, head, head
        while True:
            if fast == None or fast.next == None or fast.next.next == None:
                return None
            slow, fast = slow.next, fast.next.next
            if slow == fast: break  # meet after moved
            
        while slow != slow2:
            slow, slow2 = slow.next, slow2.next
        return slow
            
        