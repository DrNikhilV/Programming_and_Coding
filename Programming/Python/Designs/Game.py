import pygame
import turtle
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Turtle Dodge")

# Set up the turtle
turtle_screen = turtle.Screen()
turtle_screen.setup(width=screen_width, height=screen_height)
turtle_screen.tracer(0)
turtle_screen.bgcolor("black")

# Create the turtle player
player = turtle.Turtle()
player.shape("turtle")
player.color("white")
player.penup()
player.speed(0)
player.goto(0, -screen_height//2 + 50)

# Set up the obstacles
obstacles = []

def create_obstacle():
    obstacle = turtle.Turtle()
    obstacle.shape("square")
    obstacle.color("red")
    obstacle.penup()
    obstacle.speed(0)
    obstacle.shapesize(stretch_wid=1, stretch_len=3)
    x = random.randint(-screen_width//2 + 50, screen_width//2 - 50)
    y = screen_height//2 - 50
    obstacle.goto(x, y)
    obstacles.append(obstacle)

# Function to move the player turtle
def move_left():
    x = player.xcor()
    x -= 20
    if x < -screen_width//2 + 50:
        x = -screen_width//2 + 50
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 20
    if x > screen_width//2 - 50:
        x = screen_width//2 - 50
    player.setx(x)

# Pygame event loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(30)
    screen.fill((0, 0, 0))

    # Check for Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left()
            elif event.key == pygame.K_RIGHT:
                move_right()

    # Move obstacles and check for collisions
    for obstacle in obstacles:
        obstacle.sety(obstacle.ycor() - 5)
        if obstacle.ycor() < -screen_height//2 - 50:
            obstacles.remove(obstacle)
            create_obstacle()
        if player.distance(obstacle) < 20:
            print("Game Over")
            running = False

    # Draw the turtle and obstacles
    turtle_screen.update()

    # Create new obstacles
    if len(obstacles) < 5:
        create_obstacle()

# Close Pygame and Turtle
pygame.quit()
turtle_screen.bye()
