from turtle import *
speed(-1)

for i in range(3, 7, 1):
    if i == 3:
        color("blue")
    elif i == 5:
        color("blue")
    else:
        color("red")
    for n in range(i):
        forward(100)
        left(360/i)
    
