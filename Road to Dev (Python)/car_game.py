import turtle
import random
import pygame

# Initialize Pygame
pygame.init()

"""
# Load sounds
collision_sound = pygame.mixer.Sound("collision.wav")
score_sound = pygame.mixer.Sound("score.wav")
"""

# Screen setup
wn = turtle.Screen()
wn.title("Car Racing Game")
wn.bgcolor("white")
wn.setup(width=800, height=600)

# Player car
car = turtle.Turtle()
car.shape("square")
car.color("blue")
car.shapesize(stretch_wid=1, stretch_len=2)
car.penup()
car.speed(0)
car.goto(0, -250)

# Move the car left
def move_left():
    x = car.xcor()
    x -= 20
    if x < -380:
        x = -380
    car.setx(x)

# Move the car right
def move_right():
    x = car.xcor()
    x += 20
    if x > 380:
        x = 380
    car.setx(x)

# Keyboard bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

# Enemy car
enemy = turtle.Turtle()
enemy.shape("square")
enemy.color("red")
enemy.shapesize(stretch_wid=1, stretch_len=2)
enemy.penup()
enemy.speed(0)
enemy.goto(random.randint(-380, 380), 250)

# Initial speeds
player_speed = 10
enemy_speed = 5

# Score
score = 0

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Target score for speed increase
target_score = 1000

# Main game loop
while True:
    enemy.sety(enemy.ycor() - enemy_speed)

    # Check for collision
    if car.distance(enemy) < 20:
        print("Game Over!")
        #collision_sound.play()
        wn.bye()

    # Check if player car passes the enemy car
    if car.ycor() > enemy.ycor():
        score += 100
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
        enemy.goto(random.randint(-380, 380), 250)
        #score_sound.play()

    # Check if enemy car is out of screen
    if enemy.ycor() < -300:
        enemy.goto(random.randint(-380, 380), 250)

    # Gradually increase speed
    player_speed += 0.001
    enemy_speed += 0.001

    # Check for target score reached
    if score >= target_score:
        target_score += 1000  # Increase target score for the next speed increase
        player_speed += 2      # Increase player speed
        enemy_speed += 1        # Increase enemy speed

    # Adjust speed to avoid excessive speed increase
    if player_speed > 15:
        player_speed = 15
    if enemy_speed > 10:
        enemy_speed = 10

    wn.update()
