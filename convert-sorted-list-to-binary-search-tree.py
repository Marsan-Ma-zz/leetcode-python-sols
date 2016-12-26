# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

# Given a singly linked list where elements are sorted in ascending order, 
# convert it to a height balanced BST.



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        
        # [Ideas]
        # 1. use fast/slow pointer to find middle point as root, 
        #    then do recursive: left/right list as left/right branch 
        # 2. 0 -> 1 -> 2 -> 3
        
        def construct(head):
            if not head: return None
            
            # split linklist
            last, slow, fast = None, head, head.next
            while fast:
                last = slow
                slow = slow.next
                fast = fast.next
                if fast: fast = fast.next
            if last: last.next = None
            
            # construct tree
            root = TreeNode(slow.val)
            root.left = construct(head) if last else None
            root.right = construct(slow.next)
            return root
        
        return construct(head)
        
        
        