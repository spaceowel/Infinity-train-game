import turtle
import math
import random

screen = turtle.Screen()
screen.title("good_guys_shooting_bad_guys")
screen.bgcolor("black")

screen.setup(500, 700)

points = 0

score = turtle.Turtle()
score.color("red")
score.speed(0)
score.penup()
score.setposition(0, 200)
score.pendown()
score.hideturtle()
score.write(points, False, "center", ("Arial", 20, 'normal')) 

player = turtle.Turtle()
player.speed(0)
player.turtlesize(-3)
turtle.register_shape("goodguys.gif")
player.shape("goodguys.gif")
player.penup()
player.setposition(0, -200)
player.lt(90)

bullet = turtle.Turtle()
bullet.speed(0)
bullet.lt(90)
bullet.penup()
bullet.color("white");
bullet.setposition(player.xcor(), player.ycor())
bullet.hideturtle()

bulletstate = "ready"

enemy = turtle.Turtle()
enemy.speed(0)
enemy.penup()
turtle.register_shape("badguy.gif")
enemy.shape("badguy.gif")
enemy.setposition(random.randint(-140, 140), 150)

def is_Coliding(colider, colidee):
	distance = math.sqrt(math.pow(colider.xcor()-colidee.xcor(),2)+math.pow(colider.ycor()-colidee.ycor(),2))
	if distance < 15:
		return True

def move_left():
	if player.xcor() < -200:
		player.setx(player.xcor())
	else:
		player.setx(player.xcor()-30)

def move_right():
	if player.xcor() > 200:
		player.setx(player.xcor())
	else:
		player.setx(player.xcor()+30)

def fire_bullet():
	global bulletstate
	if bulletstate == "ready":
		bulletstate = "fire"
		bullet.showturtle()

turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

while(True):
	enemy.sety(enemy.ycor() - 1)
	if bulletstate != "fire":
		bullet.setposition(player.xcor(), player.ycor() - 10)

	if bulletstate == "fire":
		bullet.sety(bullet.ycor()+10)

	if bullet.ycor() >= 200 :
		bullet.sety(player.ycor())
		bulletstate = "ready"
		bullet.hideturtle()

	if is_Coliding(bullet, enemy):
		bullet.sety(player.ycor() - 10)
		bulletstate = "ready"
		bullet.hideturtle()
		enemy.setposition(random.randint(-140, 140), 150)
		points += 10
		score.clear()
		score.write(points, False, "center", ("Arial", 20, 'normal'))
	if enemy.ycor() == player.ycor():
                break
