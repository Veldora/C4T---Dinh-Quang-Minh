from turtle import *
speed(-1)

colors=["red","blue","brown","yellow","grey"]

for i in range(3,8,1):
    for n in range(i):
        forward(100)
        left(360/i)
        pencolor(colors[i-3])

mainloop()
