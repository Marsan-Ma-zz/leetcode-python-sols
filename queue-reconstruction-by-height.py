# https://leetcode.com/problems/queue-reconstruction-by-height/

# Suppose you have a random list of people standing in a queue. 
# Each person is described by a pair of integers (h, k), 
# where h is the height of the person and k is the number of people 
# in front of this person who have a height greater than or equal to h. 
# Write an algorithm to reconstruct the queue.

# Note:
# The number of people is less than 1,100.

# Example

# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]



class Solution(object):

    # from and with explaination in:
    # https://discuss.leetcode.com/topic/60981/explanation-of-the-neat-sort-insert-solution
    def reconstructQueue(self, people):
        people.sort(key=lambda (h, k): (-h, k))
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue


    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # [Example]
        # Input:
        # [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
        # Output:
        # [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

        
        # [Ideas]
        # 1. it's useless to sort only for height or priority
        # 2. brute force: process one person a time from all (x, 0)
        #    => [[7,0], [5,0]] => [[5,0], [7,0]]
        #    then the (x, 1)
        #    => [[5,0], [7,0], [6,1], [7,1]]
        #    => [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
        # 3. following this, we always place them in only possible places
        # 4. cost O(n**2) time at worst, O(n) new space
        #-------------------
        # 1. find a way just one-pass check and swap?
        # X. doesn't seems to work
        
        if not people: return []
        
        people = sorted(people, key=lambda v: (v[1], v[0]))
        # print("people", people)
        sols = [people[0]]
        for h, f in people[1:]:
            cnt = 0
            # print("sols:", sols)
            for i in range(len(sols)+1):
                if i >= len(sols):
                    sols.append((h,f))
                    break
                elif (f == cnt) and (sols[i][0] >= h):
                    sols = sols[:i] + [(h, f)] + sols[i:]
                    break
                elif sols[i][0] >= h:
                    cnt += 1
        return sols
    
    
    def test(self):
        cases = [
            [],
            [(1,0)],
            [(1,1), (3,0)],
            [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]],
            [[2,6], [3,6], [1,6], [7,0], [4,4], [7,1], [5,0], [6,1], [5,2]],
            [[3,6], [1,6], [7,0], [4,4], [7,1], [2,6], [5,0], [6,1], [5,2]],
        ]
        for c in cases:
            print(c, '=>', self.reconstructQueue(c))
                 
                
Solution().test()