from turtle import *

#build a house

#square

speed(10)
width(3)

color("green")
begin_fill()
begin_fill
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(70)
left(90)
end_fill()
end_fill()

#door

color("yellow")
begin_fill()

forward(100)
right(90)

forward(70)
right(90)

forward(100)
end_fill()

#roof

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

# 1 windows

color("black")

penup()
goto(30, 170)
pendown()

left(30)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(60)

# 2 window

penup()
goto(170, 170)
pendown()
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(30)
right(90)
forward(60)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(60)

# tree


penup()
goto(-300, -100)
pendown()
begin_fill()
color("brown")
left(90)
forward(60)
left(90)
forward(250)
left(90)
forward(60)
left(90)
forward(250)
end_fill()
left(180)
forward(250)

begin_fill()
color("lime")
left(90)
forward(130)
left(180)
forward(190)
forward(130)
left(90)
forward(100)
left(90)
forward(190)
forward(130)

left(90)
forward(100)
left(90)
forward(320)
left(90)
forward(100)
left(90)
forward(80)
right(90)
forward(100)
left(90)
forward(160)
left(90)
forward(100)
right(90)
forward(80)
end_fill()



exitonclick()