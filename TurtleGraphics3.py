import turtle
import random

Colors = ['black','yellow','pink','green','blue','gray','purple','orange', 'lightyellow']

Ngan = turtle.Turtle()
Ngan.width(3)
Ngan.color('red')
Ngan.penup()
Ngan.setpos(-600,-200)
Ngan.pendown()
def up():
	Ngan.setheading(90)
	Ngan.forward(50)

def down():
	Ngan.setheading(270)
	Ngan.forward(50)

def left():
	Ngan.setheading(180)
	Ngan.forward(50)

def right():
	Ngan.setheading(0)
	Ngan.forward(50)

def go45down():
	Ngan.setheading(-45)
	Ngan.forward(50)

def go45up():
	Ngan.setheading(45)
	Ngan.forward(50)

def clickleft(x,y):
	Ngan.color(random.choice(Colors))

def clickright(x,y):
	Ngan.stamp()


turtle.listen()
turtle.onscreenclick(clickleft,1)
turtle.onscreenclick(clickright,3)

turtle.onkey(up,'Up')
turtle.onkey(down,'Down')
turtle.onkey(left,'Left')
turtle.onkey(right,'Right')
turtle.onkey(go45down,'g')
turtle.onkey(go45up,'u')
turtle.mainloop()
