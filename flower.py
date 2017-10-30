import turtle

def DrawFlower():
	window=turtle.Screen()
	window.bgcolor("white")
	some_turtle=turtle.Turtle()
	some_turtle.shape("arrow")
	some_turtle.speed(1000000000)
	some_turtle.color("blue")
	for j in range(0,36):
		DrawTriangle(some_turtle,2)
		DrawTriangle(some_turtle,3)
		some_turtle.right(10)
	#some_turtle.right(90)	
	#some_turtle.forward(200)
	window.exitonclick()	

def DrawTriangle(brad,num):
	for i in range(0,num):
		brad.forward(100)
		brad.right(120)



DrawFlower()		