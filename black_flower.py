import turtle

def draw_square(any_turtle):
    for e in range (4):
       any_turtle.forward(100)
       any_turtle.right(90)

def draw_circle(any_turtle):
    x = 10
    for n in range(1, 50):
        any_turtle.circle(x)
        x = x + 2

def draw_shapes():
    # screen settings
    window = turtle.Screen()
    window.bgcolor("red")

    # circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.speed(12)
    x = 10
    for n in range(1, 11):
        draw_circle(angie)
        angie.right(36)
    angie.right(90)
    angie.width(10)
    angie.forward(1000)

    window.exitonclick()

draw_shapes()