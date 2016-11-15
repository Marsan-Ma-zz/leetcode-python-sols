# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

# You may not alter the values in the nodes, only nodes itself may be changed.

# Only constant memory is allowed.

# For example,
# Given this linked list: 1->2->3->4->5

# For k = 2, you should return: 2->1->4->3->5

# For k = 3, you should return: 3->2->1->4->5



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        # [Ideas]
        # 1. find kth node, make it as new head, 
        #    and record k+1 node for later connection
        # 2. reverse 1th to kth node, then next round
        # 3. if ended before kth node found, remain unchange. => O(n)
        
        if not head: return None
        if k == 1: return head
            
        node, last, blast = head, None, None
        while node:
            # check k-node batch exists
            cnode = node
            if blast: blast.next = cnode
            for _ in range(k-1):
                cnode = cnode.next
                if not cnode: return head
                
            # connect between batch
            if blast: 
                blast.next = cnode
            else:
                head = cnode
            
            # reverse batch
            blast, last = node, None
            for i in range(k):
                # node, node.next, last = node.next, last, node
                tmp = node.next
                node.next = last
                last = node
                node = tmp
                
        return head
                
                