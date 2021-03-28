import turtle
#from turtle import * #调用跟更方便
# turtle.setheading(130)
# turtle.forward(1000)
turtle.pensize(3)
turtle.pencolor('blue')
turtle.penup()
turtle.goto(-40,-40)
turtle.pendown()
turtle.speed(4)
turtle.begin_fill()
turtle.color('red')
turtle.circle(150,steps=6)
turtle.end_fill()