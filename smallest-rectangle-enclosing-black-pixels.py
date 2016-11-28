# https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/

# An image is represented by a binary matrix with 0 as a white pixel and 1 
# as a black pixel. The black pixels are connected, i.e., there is only one 
# black region. Pixels are connected horizontally and vertically. Given the 
# location (x, y) of one of the black pixels, return the area of the smallest 
# (axis-aligned) rectangle that encloses all black pixels.

# For example, given the following image:

# [
#   "0010",
#   "0110",
#   "0100"
# ]
# and x = 0, y = 2,
# Return 6.



class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        
        if not image or not image[0]: return 0

        # BFS search min/max of x/y
        m, n = len(image), len(image[0])
        max_x, min_x, max_y, min_y = x, x, y, y
        queue = [(x, y)]
        visited = set()
        for xq, yq in queue:
           max_x, min_x, max_y, min_y = max(max_x, xq), min(min_x, xq), max(max_y, yq), min(min_y, yq)           
           for di, dj in {(1,0),(-1,0),(0,1),(0,-1)}:
               xi, yi = xq+di, yq+dj
               if 0 <= xi < m and 0 <= yi < n and image[xi][yi] == '1' and (xi, yi) not in visited:
                   queue.append((xi, yi))
                   visited.add((xi, yi))
        return (max_x - min_x + 1)*(max_y - min_y + 1)


    def test(self):
        cases = [
            ([], 3,0),
            (["0010","0110","0100"], 0, 2),
        ]
        for img, x, y in cases:
            print(self.minArea(img, x, y))


# Solution().test()


