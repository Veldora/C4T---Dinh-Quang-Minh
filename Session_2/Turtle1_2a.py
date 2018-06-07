from turtle import *
speed(-1)

color("red")

right(60)
turn = 1

for i in range(4):
    left(90)
    for i in range(4):
        forward(100)
        if turn % 2 == 0:
            right(120)
        else:
            right(60)
        turn += 1
