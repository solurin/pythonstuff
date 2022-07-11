# randomboxes.py
# written by Dr. Mark Meyer
# CSC 111 8/17

import turtle as t
import random

def random_color():
	colors = "red,yellow,blue,green,cyan,brown,gray,black,orange,violet,magenta".split(",")
	return colors[random.randint(0,len(colors)-1)]

def make_square():
	make_square.round = 1-make_square.round
	x = random.randint(-500,500)
	y = random.randint(-500,500)
	size = random.randint(5,50)
	t.penup()
	t.setposition(x, y)
	t.color(random_color())
	t.begin_fill()
	if make_square.round == 1:
		t.circle(size)
	else:
		for i in range(4):
			t.fd(size)
			t.right(90)
	t.end_fill()
	t.penup()
make_square.round = 0

t.reset()
t.clear()
t.speed(0)
t.hideturtle()
for i in range(1,200):
	make_square()
	