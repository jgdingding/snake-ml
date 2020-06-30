from snakeGame import SnakeGame, direction
from gameDisplay import GameDisplay
from random import randint, choice
from time import sleep

s = SnakeGame()
gd = GameDisplay(s)

while s.snakeLength > 0:

    if randint(0, 100) > 80:
        s.changeDirection(choice(s.getPossibleDirections()))
        print(s.moveDirection)

    movement = s.moveSnake()

    gd.updateSnake(movement)

    sleep(0.5)

gd.animate()
