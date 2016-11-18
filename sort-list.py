# https://leetcode.com/problems/sort-list/

# Sort a linked list in O(n log n) time using constant space complexity.



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # [Ideas]
        # 1. find a sorting algorithm suit link list
        # 2. quicksort: pick the head, split into two link list: 
        #    into smaller than head and larger than head, recursively
        # 3. solve TLE by 3-way quicksort: keep nodes with same value 
        #    as base out of sort, directly append to base
        
        head, tail = self.quicksort(head)
        return head
    
    def quicksort(self, node):
        if not node: return None, None
        if not node.next: return node, node
        
        base_head, base_tail = node, node
        h1, h2 = None, None    # headers
        l1, l2 = None, None    # latest nodes
        node = node.next
        while node:
            # print(node.val)
            if node.val == base_head.val:
                base_tail.next = node
                base_tail = node
            elif node.val < base_head.val:
                if not h1:
                    h1, l1 = node, node
                else:
                    l1.next, l1 = node, node
            elif node.val > base_head.val:
                if not l2:
                    h2, l2 = node, node
                else:
                    l2.next, l2 = node, node
            if not node.next: break
            node.next, node = None, node.next
        
        # merge
        s1, t2, base_tail.next = base_head, base_tail, None
        if h1: 
            s1, t1 = self.quicksort(h1)
            t1.next = base_head
            
        if h2:
            s2, t2 = self.quicksort(h2)
            base_tail.next = s2
            
        return s1, t2    # head and tail
                    
                   
        