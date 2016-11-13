# https://leetcode.com/problems/design-snake-game/

# Design a Snake game that is played on a device with screen size = width x height. 
# Play the game online if you are not familiar with the game.

# The snake is initially positioned at the top left corner (0,0) with length = 1 unit.

# You are given a list of food's positions in row-column order. 
# When a snake eats the food, its length and the game's score both increase by 1.

# Each food appears one by one on the screen. For example, the second food will 
# not appear until the first food was eaten by the snake.

# When a food does appear on the screen, it is guaranteed that it will not appear 
# on a block occupied by the snake.

# Example:
# Given width = 3, height = 2, and food = [[1,2],[0,1]].

# Snake snake = new Snake(width, height, food);

# Initially the snake appears at position (0,0) and the food at (1,2).

# |S| | |
# | | |F|

# snake.move("R"); -> Returns 0

# | |S| |
# | | |F|

# snake.move("D"); -> Returns 0

# | | | |
# | |S|F|

# snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, 
# the second food appears at (0,1) )

# | |F| |
# | |S|S|

# snake.move("U"); -> Returns 1

# | |F|S|
# | | |S|

# snake.move("L"); -> Returns 2 (Snake eats the second food)

# | |S|S|
# | | |S|

# snake.move("U"); -> Returns -1 (Game over because snake collides with border)



class SnakeGame(object):

    def __init__(self, width,height,food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.width = width
        self.height = height
        self.foods = food
        self.score = 0
        self.snake = [(0, 0)]

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        cur = self.snake[-1]
        move = {
            'U': (-1, 0),
            'D': (1, 0),
            'R': (0, 1),
            'L': (0, -1),
        }[direction]
        nxt = [cur[0] + move[0], cur[1] + move[1]]
        # print("nxt", nxt)
        
        within = (0 <= nxt[0] < self.height) and (0 <= nxt[1] < self.width)
        if (not within) or (nxt in self.snake[1:]):
            if not within: print("not within")
            if (nxt in self.snake[:-1]): print(nxt, self.snake)
            return -1
        elif self.foods and (nxt == self.foods[0]):
            self.score += 1
            self.foods.pop(0)
        else:
            self.snake.pop(0)
        self.snake.append(nxt)
        print(nxt, self.score)
        return self.score
            

# cases = [
#     ('RDRULU', [[1,2],[0,1]]),
#     ('RDRULLDRR', [[1,2],[0,1], [0,0]]),
# ]
# for word, foods in cases:
#     snake = SnakeGame(3, 2, foods)
#     # print(snake.snake, word, snake.foods)
#     for c in word:
#         print(snake.move(c))


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)