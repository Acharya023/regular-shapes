import turtle
n = int(input("Type the number of sides of the shape you want\n"))
tut = turtle.Screen()
tut.bgcolor("green")
tut.title("Turtle")
geekyTurtle = turtle.Turtle()
my_pen = turtle.Turtle()
my_pen.color("orange")
tut = turtle.Screen()
for i in range(n):
    my_pen.forward(100)
    my_pen.left(360//n)
turtle.exitonclick()
