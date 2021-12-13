import turtle as t
import time
import winsound

# create window

wn = t.Screen()
wn.title("Squid Game")
wn.bgcolor("lightblue")
wn.bgpic("bg1.gif")
wn.setup(width = 700, height = 700)
wn.register_shape("idle.gif")
wn.register_shape("walk1.gif")
wn.register_shape("walk2.gif")
wn.register_shape("walk3.gif")
wn.register_shape("walk4.gif")
wn.register_shape("dollfront.gif")
wn.register_shape("dollback.gif")


# pen object
pen = t.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.goto(0,290)


light = t.Turtle()
#light.hideturtle()
light.speed(0)
light.shape("circle")
light.shapesize(3)
light.color("yellow")
light.penup()
light.goto(230,270)

light1 = t.Turtle()
#light1.hideturtle()
light1.speed(0)
light1.shape("circle")
light1.shapesize(3)
light1.color("yellow")
light1.penup()
light1.goto(230,-270)

doll = t.Turtle()
doll.hideturtle()
doll.shape('dollback.gif')
doll.penup()
doll.goto(230, 30)

def draw():
	wn.bgpic("gamebg.gif")
	# t.goto(150,300)

	light.showturtle()
	doll.showturtle()
	light1.showturtle()
	p1.showturtle()

#player1
p1 = t.Turtle()
p1.hideturtle()
p1.shape('idle.gif')
p1.shapesize(20,20)
p1.penup()
p1.goto(-290,120)
p1.speed(3)

def fwd():
	p1.forward(10)
	if (p1.shape() == "idle.gif"):
		p1.shape("walk1.gif")
	elif (p1.shape() == "walk1.gif"):
		p1.shape("walk2.gif")
	elif (p1.shape() == "walk2.gif"):
		p1.shape("walk3.gif")
	elif (p1.shape() == "walk3.gif"):
		p1.shape("walk1.gif")
	# elif (p.shape() == "walk4.gif"):
	# 	p.shape("idle.gif")


def check(post):
    players = [p1]
    for i in range(len(players)):
        curr = players[i].xcor()
        prev = post[i]
        if curr > prev:
            # players[i].hideturtle()
            print("!! PLAYER OUT !!")
            print('difference == ', curr-prev)
            y = players[i].ycor()
            pen.goto(0,0)
            pen.write("!!PLAYER OUT!!", align="center", font=("Courier",24,"bold"))
            players[i].penup()
            players[i].hideturtle()

def sound():
	winsound.PlaySound('RLGL.wav',winsound.SND_ASYNC)
	draw()
	run()

def wtv():
	print("------------------------------------------")

wn.listen()
wn.onkeypress(fwd,'Return')
wn.onkeypress(sound,'space')
wn.onkeypress(wtv,'m')

def run():
	ft = time.time() + 1
	while True:
		wn.update()
		t = time.time() - ft 
		rst = 5
		if t < 60:
			print("t = ",t)

			if (t > 4.2 and t < 12):
				check(post)
				light.color("red")
				light1.color("red")
				doll.shape("dollfront.gif")
			else:
				post = [p1.xcor()]
				light.color("green")
				light1.color("green")
				doll.shape("dollback.gif")

			if (t > 12):
				ft = time.time()
				pen.clear()

			if p1.xcor() > 150:
				pen.goto(0,0)
				pen.write(" CONGRATS YOU WIN !",align="center",font=("Courier",24,"bold"))

while True:
	wn.update()