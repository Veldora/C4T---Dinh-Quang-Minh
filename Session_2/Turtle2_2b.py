from turtle import *
speed(-1)

colors=["red","blue","brown","yellow","grey"]

for i in range(5):
        color(colors[i])
        begin_fill()
        
        for x in range(2):
            forward(50)
            right(90)
            forward(100)
            right(90)
            
        forward(50)
        end_fill()
