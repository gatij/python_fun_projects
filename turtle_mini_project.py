import turtle


def DrawDesign():
	window=turtle.Screen()
	window.bgcolor("red")
	obj_turtle=turtle.Turtle()
	for j in range(0,36):
		DrawSquare(obj_turtle)
	window.exitonclick()

def DrawSquare(some_turtle):
	some_turtle.shape("arrow")
	some_turtle.color("yellow")
	some_turtle.speed(5)
	for i in range(0,4):
		some_turtle.forward(100)
		some_turtle.right(90)

	some_turtle.right(10)	

	
DrawDesign()		