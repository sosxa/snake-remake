from snake import Snake
from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard

# screen setup
screen = Screen()
screen.setup(width= 600, height=600)
screen.bgcolor("black")
screen.title("Snake Remake")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
	# updating the screen when the movement is done so it looks cleaner 
	screen.update()
	# making the blocks move faster 
	time.sleep(0.1)
	snake.move()
# when its 15 pixels or less away in contact from the head it calls refresh which generates a new random location, also since the food is 10 x 10 px
	if snake.head.distance(food) < 15:
		food.refresh()
		snake.extend()
		scoreboard.increase()
# detect collision with wall
	if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
		# 280 away from each corner cant be 300 since the  snake blocks  are 20px
		game_is_on = False
		scoreboard.game_over()

	# detect collision with tail
    # if head collides with tail
    # game over
	for block in snake.blocks[1:0]:
		# so the  game doesnt just instantly make you lose since you start as the snake head obviously
		if snake.head.distance(block) < 10:
			# 10 because the snake is 20 px so if you get 1/2 of the way to touching your tail or another block from your snake you lose
			game_is_on = False
			scoreboard.game_over()

screen.exitonclick()