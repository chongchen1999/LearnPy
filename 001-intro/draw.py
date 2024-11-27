import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=400, height=200)

# Function to draw a ring
def draw_ring(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.width(5)
    turtle.circle(50)

# Draw Olympic rings
colors = ["blue", "yellow", "black", "green", "red"]
positions = [
    (-150, -50),   # Blue
    (-75, 0),      # Yellow
    (0, -50),      # Black
    (75, 0),       # Green
    (150, -50)     # Red
]

# Draw each ring
for color, pos in zip(colors, positions):
    draw_ring(pos[0], pos[1], color)

# Hide the turtle and keep the window open
turtle.hideturtle()
screen.mainloop()