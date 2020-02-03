"""bouncing shapes"""

import turtle
import random
import pyinputplus as p

#screen
sc = turtle.Screen()
sc.bgcolor("black")
sc.setup(width=800, height=600)
sc.title("bouncing balls")
sc.tracer(0)

#list of color
list_of_colors = ["red", "orange", "purple", "white", "yellow", "blue", "green"]

#list of shapes
list_of_shapes = ["square", "triangle", "circle"]

#prompt for a number of shapes 
prompt_for_number = p.inputInt("Enter a number from 1 to 500: ", min=1, max=500)

#create shapes
number_of_shapes  = []
for i in range(prompt_for_number):
    number_of_shapes.append(turtle.Turtle())

for shape in number_of_shapes:
    shape.color(random.choice(list_of_colors))
    shape.shape(random.choice(list_of_shapes))
    shape.penup()
    x = random.randint(-400, 400)
    y = random.randint(-300, 300)
    shape.goto(x, y)
    shape.dx = random.randint(-3, 3)
    shape.dy = 0
    shape.da = random.randint(-5, 5)

#create gravity
gravity = 0.1

#main loop
while True:

    sc.update()

    for shape in number_of_shapes:

        #use gravity
        shape.dy -= gravity

        #rotate
        shape.rt(shape.da)

        #make the shapes move
        shape.sety(shape.ycor() + shape.dy)

        shape.setx(shape.xcor() + shape.dx)

        #make the shapes bounce off the edges
        if shape.ycor() < - 300:
            shape.sety(-300)
            shape.dy *= -1
            shape.da *= -1

        if shape.ycor() > 300:
            shape.sety(300)
            shape.dy *= -1
            shape.da *= -1

        if shape.xcor() < -400:
            shape.setx(-400)
            shape.dx *= -1
            shape.da *= -1

        if shape.xcor() > 400:
            shape.setx(400)
            shape.dx *= -1
            shape.da *= -1








