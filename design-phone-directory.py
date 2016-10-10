# https://leetcode.com/problems/design-phone-directory/

# Design a Phone Directory which supports the following operations:

# get: Provide a number which is not assigned to anyone.
# check: Check if a number is available or not.
# release: Recycle or release a number.
# Example:

# // Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
# PhoneDirectory directory = new PhoneDirectory(3);

# // It can return any available phone number. Here we assume it returns 0.
# directory.get();

# // Assume it returns 1.
# directory.get();

# // The number 2 is available, so return true.
# directory.check(2);

# // It returns 2, the only number that is left.
# directory.get();

# // The number 2 is no longer available, so return false.
# directory.check(2);

# // Release number 2 back to the pool.
# directory.release(2);

# // Number 2 is available again, return true.
# directory.check(2);


class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.max_n = maxNumbers
        self.nums = {i for i in range(self.max_n)}

        
    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        return -1 if not self.nums else self.nums.pop()
            
        

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return (number in self.nums)

    
    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        if len(self.nums) >= self.max_n:
            pass
        elif number >= self.max_n:
            pass
        elif (number not in self.nums):
            self.nums |= {number}
        

def test():
    obj = PhoneDirectory(3)
    print(obj.nums)
    n1 = obj.get()
    print(n1)
    print(obj.check(n1))
    print(obj.release(n1))
    print(obj.check(n1))
    n1 = 5    
    print(obj.check(n1))
    print(obj.release(n1))
    print(obj.check(n1))
    
# test()
