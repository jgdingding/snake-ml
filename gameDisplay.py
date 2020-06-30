from tkinter import Canvas
from tkinter import Tk
from snakeGame import direction, SnakeGame


class GameDisplay:

    def __init__(self, sg):
        self.gameInstance = sg
        self.snakeLayer = []
        self.foodLayer = []

        # initialize tkinter elements
        self.root = Tk()
        self.root.geometry('500x500')
        self.canvas = Canvas(self.root, width=500, height=500)  # w

        self.drawBoard()

    def drawBoard(self):
        self.canvas.create_line(50, 50, 50, 450)
        self.canvas.create_line(450, 450, 450, 50)
        self.canvas.create_line(50, 50, 450, 50)
        self.canvas.create_line(50, 450, 450, 450)

        for i in range(70, 450, 20):
            self.canvas.create_line(i, 50, i, 450)

        for j in range(70, 450, 20):
            self.canvas.create_line(50, j, 450, j)

        for i in range(len(self.gameInstance.snake)):
            if i > 0:
                self.snakeLayer.append(self.canvas.create_oval(
                    self.gameInstance.snake[i][0]*20+44, self.gameInstance.snake[i][1]*20+44, 
                    self.gameInstance.snake[i][0]*20+56, self.gameInstance.snake[i][1]*20+56, fill="black"))
            else:
                self.snakeLayer.append(self.canvas.create_oval(
                    self.gameInstance.snake[i][0]*20+44, self.gameInstance.snake[i][1]*20+44, 
                    self.gameInstance.snake[i][0]*20+56, self.gameInstance.snake[i][1]*20+56, fill="blue"))

        self.foodLayer.append(self.canvas.create_oval(
            self.gameInstance.food[0]*20+44, self.gameInstance.food[1]*20+44, 
            self.gameInstance.food[0]*20+56, self.gameInstance.food[1]*20+56, fill="red"))
        self.canvas.pack()

        self.root.update()
        return

    # Redraws snake and food
    def updateSnake(self, movement):
        if movement == -1:
            moveme = self.foodLayer.pop()
            self.canvas.itemconfig(moveme, fill="blue")
            self.snakeLayer.insert(0, moveme)
            self.canvas.itemconfig(self.snakeLayer[1], fill="black")
            self.foodLayer.append(self.canvas.create_oval(
                self.gameInstance.food[0]*20+44, self.gameInstance.food[1]*20+44, 
                self.gameInstance.food[0]*20+56, self.gameInstance.food[1]*20+56, fill="red"))

        elif movement == 1:
            moveme = self.snakeLayer.pop()
            self.canvas.itemconfig(moveme, fill="blue")
            x = ((self.gameInstance.snake[0][0]) 
                - int((self.canvas.coords(moveme)[0] - 44)/20)) * 20
            y = ((self.gameInstance.snake[0][1]) 
                - int((self.canvas.coords(moveme)[1] - 44)/20)) * 20
            self.canvas.move(moveme, x, y)
            self.snakeLayer.insert(0, moveme)
            self.canvas.itemconfig(self.snakeLayer[1], fill="black")

        self.root.update()
        return

    def animate(self):
        self.root.mainloop()
