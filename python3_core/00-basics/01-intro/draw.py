import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
olympic_ring = turtle.Turtle()
olympic_ring.speed(3)

# Function to draw a ring
def draw_ring(x, y, color):
    olympic_ring.penup()
    olympic_ring.goto(x, y)
    olympic_ring.pendown()
    olympic_ring.color(color)
    olympic_ring.circle(50)

# Draw the Olympic rings
draw_ring(-120, 0, "blue")
draw_ring(0, 0, "black")
draw_ring(120, 0, "red")
draw_ring(-60, -60, "yellow")
draw_ring(60, -60, "green")

# Hide the turtle and display the result
olympic_ring.hideturtle()
turtle.done()