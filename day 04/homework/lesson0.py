print ("nika korinteli")


from turtle import *
#we want to paint house

#step 1: draw a square
speed(7)
width(7)
color("brown")
forward(200)
left(90)


forward(200)
left(90)


forward(200)
left(90)


forward(200)
left(90)


#end square 

#drawing a door

forward(70)
color("black")
begin_fill()
left(90)
forward(120) #height of the door 
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("blue")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of square

penup()
goto (190, 190)
pendown()

color ("black")
begin_fill()
right(60)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()


penup()
goto(10, 190)
pendown()


color("black")
begin_fill()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()


exitonclick