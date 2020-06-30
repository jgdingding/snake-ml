from snakeGame import SnakeGame, direction
from gameDisplay import GameDisplay
from random import randint, choice
from time import sleep

s = SnakeGame()
gd = GameDisplay(s)

while s.snakeLength > 0:
    # if randint(0, 100) > 75:
    s.changeDirection(direction.up)
    #     print("direction changed")

    movement = s.moveSnake()
    gd.updateSnake(movement)

    print(s.snake)

    sleep(0.5)
gd.animate()
