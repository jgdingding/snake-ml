# Architecture of snake game
# Justin Gou and William Yao 6/27/2020
#
# Creates and displays the board and snake
# Implements functions to update the board and snake
from enum import Enum

import random


class direction(Enum):
    right = (1, 0)
    left = (-1, 0)
    up = (0, 1)
    down = (0, -1)


class items(Enum):
    blank = 0
    snake = 1
    food = 2


class SnakeGame:

    boardSize = 20
    snake = [(5, 10), (4, 10), (3, 10)]  # 0th element represents head
    snakeLength = 3
    facing = direction.right

    food = (15, 10)

    def __init__(self):
        self.board = [[items.blank.value]*20]*20

    def moveSnake(self, dtn):
        newCoord = (self.snake[0][0] + dtn[0],
                    self.snake[0][1] + dtn[1])
        if newCoord[0] == self.food[0] and newCoord[1] == self.food[1]:  # if we hit the food
            self.snake.insert(0, newCoord)
            self.snakeLength += 1
            self.generateFood()
            self.board[newCoord[0]][newCoord[1]] = items.snake.value
            return -1
        # check if snake goes out of bounds or hits own tail
        elif newCoord in self.snake or newCoord[0] > 19 or newCoord[0] < 0 or newCoord[1] > 19 or newCoord[1] < 0:
            self.snakeLength = 0
            return 0
        else:
            self.snake.insert(0, newCoord)
            oldTail = self.snake.pop()
            self.board[oldTail[0]][oldTail[1]] = items.blank.value
            self.board[newCoord[0]][newCoord[1]] = items.snake.value
            return 1
        return 0

    def generateFood(self):
        self.board[self.food[0]][self.food[1]] = items.blank.value
        x = random.randint(0, 19)
        y = random.randint(0, 19)
        while (x, y) in self.snake:
            x = random.randint(0, 19)
            y = random.randint(0, 19)
        self.food = (x, y)
        self.board[x][y] = items.food.value
        return
