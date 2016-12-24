# https://leetcode.com/problems/add-two-numbers-ii/

# You are given two linked lists representing two non-negative numbers. 
# The most significant digit comes first and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

# Example:

# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # linklist to stack
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
            
        if len(stack1) < len(stack2):
            stack1, stack2 = stack2, stack1
            
        # add-up
        last, ci = None, 0 
        while stack1:
            a = stack1.pop()
            b = stack2.pop() if stack2 else 0
            s = a + b + ci
            ci = s // 10
            node = ListNode(s % 10)
            node.next, last = last, node
        if ci:
            node = ListNode(ci)
            node.next, last = last, node
        return last
        