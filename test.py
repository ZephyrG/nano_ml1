import turtle

def draw_squre(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(20)
    for i in range(0, 140):
        draw_squre(brad)
        brad.right(3)

    window.exitonclick()

draw_art()
