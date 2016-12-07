# https://leetcode.com/problems/implement-stack-using-queues/

# Implement the following operations of a stack using queues.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.
# Notes:
# You must use only standard operations of a queue -- which means only push 
# to back, peek/pop from front, size, and is empty operations are valid.
# Depending on your language, queue may not be supported natively. You may 
# simulate a queue by using a list or deque (double-ended queue), as long as 
# you use only standard operations of a queue.
# You may assume that all operations are valid (for example, no pop or top 
# operations will be called on an empty stack).

# Update (2015-06-11):
# The class name of the Java function had been updated to MyStack instead of Stack.



# [Ideas]
# 1. queue is natively good for push, empty. => need pop, top
#    => while pop/top, always pop and push immediately n-1 time
#    => if we need to reorder/reverse, need two extra queue with many steps
#    Ex: queue1 = [1, 2, 3, 4]
#        queue2 = [1, 2, 3], queue1 = [4]
# 2. only two state: q1 has all value, or q1 has some value and frontier in q2


class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q1, self.q2 = [], []
        


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q1.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        sol = self.q1.pop(0)
        self.q1, self.q2 = self.q2, self.q1
        return sol


    def top(self):
        """
        :rtype: int
        """
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        return self.q1[0]




    def empty(self):
        """
        :rtype: bool
        """
        return (len(self.q1) + len(self.q2) == 0)


