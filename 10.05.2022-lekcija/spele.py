import turtle

wn=turtle.Screen()
wn.title('Clicker')
wn=turtle.bgcolor('black')

wn.register_shape('cookie.gif')

cookie=turtle.Turtle()
cookie=turtle.shape('cookie.gif')
cookie.speed(0)

clicks=0

pen=turtle.Turtle()
pen.hideturtle()

pen.color("white")
pen.goto(0,200)
pen.write(f"Clicks:{clicks}",align="center",font=("Courier New",12,"normal"))

def click(x,y):
    global clicks
    clicks+=1
    pen.clear()
    pen.write(f"Clicks:{clicks}",align="center",font=("Courier New",32,"normal"))

cookie.onclick(click)


wn.mainloop()