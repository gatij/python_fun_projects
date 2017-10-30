import turtle

def DrawSquare(brad):
	#window=turtle.Screen()
	#window.bgcolor("red")
	#brad=turtle.Turtle()
	brad.shape("turtle")
	brad.color("green")
	brad.speed(2)
	for i in range(0,4):
		brad.forward(100)
		brad.right(90)
	brad.right(15)	
	#DrawCircle()
	#DrawTriangle()	

	#window.exitonclick()


def DrawCircle():
	alice=turtle.Turtle()
	alice.shape("arrow")
	alice.color("blue")
	alice.circle(100)
	



def DrawTriangle():
	bob=turtle.Turtle()
	for i in range(0,3):
		bob.forward(100)
		bob.right(120)

def Draw():
	window=turtle.Screen()
	window.bgcolor("red")
	SomeTurtle=turtle.Turtle()
	DrawSquare(SomeTurtle)
	DrawCircle()
	DrawTriangle()
	window.exitonclick()



#Draw()	


	




#def DrawShapes():
	#DrawSquare()
	#DrawCircle()
	#DrawTriangle()
	

#DrawSquare()	



	

