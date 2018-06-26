from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

turtle.forward(1)
count = 0

for i in range(0,500):
    turtle.left(10)
    turtle.forward(i/10)

    
screen.exitonclick()
