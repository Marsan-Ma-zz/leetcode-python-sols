# https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/

# The API: int read4(char *buf) reads 4 characters at a time from a file.

# The return value is the actual number of characters read. For example, 
# it returns 3 if there is only 3 characters left in the file.

# By using the read4 API, implement the function int read(char *buf, int n) 
# that reads n characters from the file.

# Note:
# The read function may be called multiple times.


# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    
    def __init__(self):
        self.queue = [] # global "buffer"
    
    def read(self, buf, n):
        idx = 0
    
        # if queue is large enough, read from queue
        while self.queue and n > 0:
            buf[idx] = self.queue.pop(0)
            idx += 1
            n -= 1
        
        while n > 0:
            # read file to buf4
            buf4 = [""]*4
            l = read4(buf4)
    
            # if no more char in file, return
            if not l:
                return idx
    
            # if buf can not contain buf4, save to queue
            if l > n:
                self.queue += buf4[n:l]
    
            # write buf4 into buf directly
            for i in range(min(l, n)):
                buf[idx] = buf4[i]
                idx += 1
                n -= 1
        return idx
        