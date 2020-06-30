from snakeGame import SnakeGame, direction
from gameDisplay import GameDisplay
from random import randint, choice
from time import sleep

s = SnakeGame()
gd = GameDisplay(s)

while s.snakeLength > 0:
    sleep(2)

    s.changeDirection(direction.right)

    movement = s.moveSnake()

    gd.updateSnake(movement)

gd.animate()
