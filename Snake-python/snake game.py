import turtle
import time
import random

delay = 0.1

# score
score = 0
high_score = 0

# window
win = turtle.Screen()
win.title("Snake game")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.fillcolor("yellow")
head.direction = "stop"

# snake fruit
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("circle")
fruit.color("red")
fruit.penup()
fruit.goto(0, 100)
fruit_number = 1
fruit_score = 1
tails = []

# score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.shapesize(stretch_wid=0.001, stretch_len=25)
pen.color("white")
pen.penup()
pen.goto(0, 250)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))


# move functions
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


# keyboard binding

win.listen()
win.onkeypress(go_up, "Up")
win.onkeypress(go_down, "Down")
win.onkeypress(go_right, "Right")
win.onkeypress(go_left, "Left")

# gameloop
while True:
    # special score
    if fruit_number == 5:
        fruit_score = 2
        fruit.color("green")
        fruit.shapesize(0.9)
    elif fruit_number == 9:
        fruit_score = 3
        fruit.color("blue")
        fruit.shapesize(0.8)

    elif fruit_number == 14:
        fruit_score = 4
        fruit.color("violet")
        fruit.shapesize(0.7)

    elif fruit_number == 19:
        fruit_score = 5
        fruit.color("orange")
        fruit.shapesize(0.6)
    else:
        fruit_score = 1
        fruit.shapesize(1)
        fruit.color("red")
    win.update()
    # collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # hide tails
        for tail in tails:
            tail.goto(1000, 1000)
        # clear the tails
        tails.clear()
        # reset the score
        score = 0
        fruit_number = 0
        # reset the delay
        delay = 0.1
        pen.clear()
        pen.write("Score: {} High score {}".format(str(score), str(high_score)), align="center",
                  font=("Courier", 24, "normal"))
        pen.goto(0, 250)

    # check collision with the fruit
    if head.distance(fruit) < 20:
        # move fruit to new random pos
        fruit_number += 1
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        fruit.goto(x, y)

        # add new tail
        new_tail = turtle.Turtle()
        new_tail.speed(0)
        new_tail.shape("square")
        new_tail.color("grey")
        new_tail.penup()
        tails.append(new_tail)

        # speed up the snake
        delay -= 0.001
        # increase the score
        score = score + fruit_score
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score: {} ".format(str(score), str(high_score)), align="center",
                  font=("Courier", 24, "normal"))
        pen.goto(0, 250)
    # move the end segments(tails) first in reverse order
    for index in range(len(tails) - 1, 0, -1):
        x = tails[index - 1].xcor()
        y = tails[index - 1].ycor()
        tails[index].goto(x, y)
    # move segment(tail) 0 to where the head is
    if len(tails) > 0:
        x = head.xcor()
        y = head.ycor()
        tails[0].goto(x, y)
    move()

    # check the head collision with the tails
    for tail in tails:
        if tail.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # hide the tails
            for tail in tails:
                tail.goto(1000, 1000)
            # clear the tails
            tails.clear()
            # reset score
            score = 0
            # reset delay
            delay = 0.1
            # update the score display
            pen.clear()
            pen.write("Score: {} High Score: {}".format(str(score), str(high_score)), align="center",
                      font=("Courier", 24, "normal"))
            pen.goto(0, 250)

    time.sleep(delay)
win.mainloop()
