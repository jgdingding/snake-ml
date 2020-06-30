from tkinter import *
from snakeGame import *
from time import *

snakee = []
foood = []
def drawBoard(root, s, w):
    for i in range(len(s.snake)):
        if i > 0:
            snakee.append(w.create_oval(s.snake[i][0]*20+44,s.snake[i][1]*20+44,s.snake[i][0]*20+56, s.snake[i][1]*20+56, fill = "black"))
        else:
            snakee.append(w.create_oval(s.snake[i][0]*20+44,s.snake[i][1]*20+44,s.snake[i][0]*20+56, s.snake[i][1]*20+56, fill = "blue"))

    foood.append(w.create_oval(s.food[0]*20+44, s.food[1]*20+44, s.food[0]*20+56, s.food[1]*20+56, fill = "red"))
    w.pack()

    return

def updateSnake(root, s, w, direct):
    sleep(0.5)
    for i in direction:
        if direct == i.name:
            val = s.moveSnake(i.value)
            if val == -1:
                snakee.insert(0, w.itemconfig(foood.pop(), fill = "blue"))
                w.itemconfig(snakee[1], fill = "black")
                foood.append(w.create_oval(s.food[0]*20+44, s.food[1]*20+44, s.food[0]*20+56, s.food[1]*20+56, fill = "red"))

            elif val == 1:
                moveme = snakee.pop()
                w.itemconfig(moveme, fill = "blue")
                x = ((s.snake[0][0] + i.value[0]) * 20) - (s.snake[-1][0] * 20)
                y = ((s.snake[0][1] + i.value[1]) * 20) - (s.snake[-1][1] * 20)
                w.move(moveme, x, y)
                snakee.insert(0, moveme)
                w.itemconfig(snakee[1], fill = "black")
    root.update()
    return

def main():
    root = Tk()
    root.geometry('500x500')
    
    w = Canvas(root, width = 500, height = 500)

    line = w.create_line(50,50,50,450)
    line = w.create_line(450,450,450,50)
    line = w.create_line(50,50,450,50)
    line = w.create_line(50,450,450,450)

    for i in range(70, 450, 20):
        line = w.create_line(i,50,i,450)

    for j in range(70, 450, 20):
        line = w.create_line(50,j,450,j)

    s = SnakeGame()

    drawBoard(root, s, w)
    root.update()
    direct = "right"
    updateSnake(root, s, w, direct)
    direct = "right"
    updateSnake(root, s, w, direct)
    direct = "right"
    updateSnake(root, s, w, direct)    
    direct = "right"
    updateSnake(root, s, w, direct)
    direct = "right"
    updateSnake(root, s, w, direct)    
    direct = "right"
    updateSnake(root, s, w, direct)    
    direct = "right"
    updateSnake(root, s, w, direct)    
    direct = "right"
    updateSnake(root, s, w, direct)
    direct = "right"
    updateSnake(root, s, w, direct)
    direct = "right"
    updateSnake(root, s, w, direct)
    root.mainloop()

main()