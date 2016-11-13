# https://leetcode.com/problems/walls-and-gates/

# You are given a m x n 2D grid initialized with these three possible values.

# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 
# to represent INF as you may assume that the distance to a gate is less 
# than 2147483647.

# Fill each empty room with the distance to its nearest gate. If it is 
# impossible to reach a gate, it should be filled with INF.

# For example, given the 2D grid:
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF

# After running your function, the 2D grid should be:
#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4



# 1:42
class Solution(object):


    # very tricky sol
    def wallsAndGates(self, rooms):
        q = [(i, j) for i, row in enumerate(rooms) for j, r in enumerate(row) if not r]
        for i, j in q:
            for I, J in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= I < len(rooms) and 0 <= J < len(rooms[0]) and rooms[I][J] > 2**30:
                    rooms[I][J] = rooms[i][j] + 1
                    q += (I, J),


    # normal sol
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.

        1. from all gates, do DFS and update accesible nodes. time: O(m*n)
            a. stop if -1, or value to update > existing number
        """
        # 0. boundary case
        if (len(rooms) == 0) or (len(rooms[0]) == 0):
            return

        # 1. find doors O(m*n)
        doors = []
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    doors.append((i,j))


        # 2. propagate from doors O(m*n*d)
        for di, dj in doors: 
            stack = []
            stack.append((di, dj))
            while stack:
                i, j = stack.pop()
                cur_step = rooms[i][j] + 1
                # up
                if (i > 0) and (rooms[i-1][j] > cur_step):
                    rooms[i-1][j] = cur_step
                    stack += [(i-1, j)]
                # down
                if (i < m-1) and (rooms[i+1][j] > cur_step):
                    rooms[i+1][j] = cur_step
                    stack += [(i+1, j)]
                # left
                if (j > 0) and (rooms[i][j-1] > cur_step):
                    rooms[i][j-1] = cur_step
                    stack += [(i, j-1)]
                # right
                if (j < n-1) and (rooms[i][j+1] > cur_step):
                    rooms[i][j+1] = cur_step
                    stack += [(i, j+1)]

    def unit_test(self):
        inf = 2147483647
        cases = [
            [],
            [[]],
            [[0]],
            [[0,-1],[-1,0]],
            [[0,-1,inf],[-1,inf,inf],[0,inf,-1]],
            [[inf,-1,0,inf], [inf,inf,inf,-1], [inf,-1,inf,-1], [0,-1,inf,inf]],
        ]
        for case in cases:
            print("before:", case)
            self.wallsAndGates(case)
            print("after:", case)
