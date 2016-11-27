# https://leetcode.com/problems/number-of-islands-ii/

# A 2d grid map of m rows and n columns is initially filled with water. 
# We may perform an addLand operation which turns the water at position 
# (row, col) into a land. Given a list of positions to operate, count the 
# number of islands after each addLand operation. An island is surrounded 
# by water and is formed by connecting adjacent lands horizontally or 
# vertically. You may assume all four edges of the grid are all surrounded by water.

# Example:

# Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
# Initially, the 2d grid grid is filled with water. (Assume 0 represents 
# water and 1 represents land).

# 0 0 0
# 0 0 0
# 0 0 0
# Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

# 1 0 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

# 1 1 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

# 1 1 0
# 0 0 1   Number of islands = 2
# 0 0 0
# Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

# 1 1 0
# 0 0 1   Number of islands = 3
# 0 1 0
# We return the result as an array: [1, 1, 2, 3]

# Challenge:

# Can you do it in time complexity O(k log mn), where k is the length of the positions?




class Solution(object):


    # shorter, elegant
    def numIslands2(self, m, n, positions):
        pa = {}
        
        def get_root(key):
            root = key
            while pa[root] != root:
                root = pa[root]
            while pa[key] != key:
                nxt = pa[key]
                pa[key] = root
                key = nxt
            return root
            
        ans = []
        
        for x, y in positions:
            if (x, y) in pa:
                ans.append(ans[-1])
            else:
                neighbors = {get_root(p) for p in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] if p in pa}
                ans.append(ans[-1] + 1 - len(neighbors))
                pa[(x, y)] = (x, y)
                for nx, ny in neighbors:
                    pa[(nx, ny)] = (x, y)
                    
        return ans[1:]


    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        
        # [Ideas]
        # 1. everytime add one land, we check surrounding 4 lands by
        #    do DFS/BFS, see if they are connected without current added land
        # --------------
        # 1. mark not connected end with different number, thus we only need
        #    to check how many numbers surrounding new land.
        # 2. if different number land exists, propage and make them united 
        #    under one mark
        # 3. use extra set to record current land numbers
        # 4. if no surrounded area => new mark created.
        #    worst case: update whole map in O(m*n)
        #---------------
        # 1. there are algorithm “Union Find” could done in O(k*log(m*n))
        #    https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf
        # 2. main idea is lazy connect numbers with tree
        # 3. to make tree as flat as possible, always append small trees root
        #    to tallest tree root
        # 4. count would be either +1 or - (merged_lands_cnt - 1)
        
        def get_neighbors(i, j):
            return [(i+di, j+dj) for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]
                      if 0 <= i+di < m and 0 <= j+dj < n 
                      and fields[i+di][j+dj] != None]
        
        def find_root(n):
            t = n
            while t in conns:
                t = conns[t]
            while (n in conns) and (conns[n] != t):
                n, conns[n] = conns[n], t
            return t
        
        conns, latest = {}, 0
        fields = [[None]*n for _ in range(m)]
        sols = [0]

        for px, py in positions:
            ns = get_neighbors(px, py)
            if not ns:
                fields[px][py] = latest
                latest += 1
                cnt = sols[-1] + 1
            else:
                roots = {find_root(fields[nx][ny]) for nx, ny in ns}
                cnt = sols[-1] - (len(roots)-1)
                top = roots.pop()
                for r in roots:
                    conns[r] = top
                fields[px][py] = top
            # calculate numIslands
            # print(conns)
            sols.append(cnt)
        # print(conns)
        return sols[1:]
        
    def test(self):
        cases = [
            (0, 0, []),
            (3, 3, [[0,0], [0,1], [1,2], [2,1]]),
            (3, 3, [[0,0], [0,1], [1,2], [2,1], [1,1]]),
            (3, 3, [[0,0], [0,1], [1,2], [2,1], [1,1], [2,2]]),
            (3, 3, [[0,0], [0,1], [1,2], [2,1], [2,2]]),
        ]
        for m, n, pos in cases:
            print(self.numIslands2(m, n, pos))

# Solution().test()
