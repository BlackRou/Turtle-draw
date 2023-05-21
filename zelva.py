from turtle import shape, forward, left, right, back, clear, exitonclick, penup, pendown

shape('turtle')

for x in range(6):

    for i in range(6):
        forward(50)
        left(60)

    left(120)
    forward(50)
    right(60)

left(120)

for _ in range(3):
    forward(50)
    left(60)

right(120)
forward(50)
right(180)

exitonclick()

