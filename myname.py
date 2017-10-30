import turtle

def DrawName():
	window=turtle.Screen()
	window.bgcolor("white")
	obj_turtle=turtle.Turtle()
	obj_turtle.shape("turtle")
	obj_turtle.color("black")
	obj_turtle.forward(100)
	obj_turtle.backward(100)
	obj_turtle.right(90)
	obj_turtle.forward(100)
	obj_turtle.right(270)
	obj_turtle.forward(100)
	obj_turtle.right(270)
	obj_turtle.forward(50)
	obj_turtle.right(270)
	obj_turtle.forward(50)

	window.exitonclick()

DrawName()	