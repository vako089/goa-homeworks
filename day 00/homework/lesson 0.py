from turtle import *


#we want to paint a house

#step 1:  draw a squar
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left (90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door
forward(70)
color("yellow")
begin_fill()

color("yellow")
left(90)
forward(120)        #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a window
penup()
goto(150, 150)
pendown()
color("brown")
right(60)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)

penup()
goto(70 , 150)
pendown()
color("brown")
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)

exitonclick()