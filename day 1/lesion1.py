from turtle import *

#we want to paint a house

#step1 draw a square
speed(20)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of sqeare

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
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

penup()
goto(185, 185)
pendown()

color("brown")
begin_fill()
left(30)
forward(70)
right(90)
forward(40)
right(90)
forward(70)
right(90)
forward(40)
end_fill()

penup()
goto(15, 185)
pendown()

color("brown")
begin_fill()
right(0)
forward(40)
right(90)
forward(70)
right(90)
forward(40)
right(90)
forward(70)
end_fill()

exitonclick()