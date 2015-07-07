import turtle
import random

def draw_square(a_turtle):
    for i in range(1,5):
        a_turtle.color(random.random(),random.random(), random.random())
        a_turtle.forward(100)
        a_turtle.right(90)



def draw_flower():
    window= turtle.Screen()
    window.bgcolor("green")
    tunki = turtle.Turtle()
    tunki.color("blue")
    tunki.speed(5)
    for i in range(1,37):
        draw_square(tunki)
        tunki.right(10)
    window.exitonclick()

draw_flower()
