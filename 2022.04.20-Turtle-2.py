import turtle as t

t.shape('arrow')
t.bgcolor('light green')
t.title('Bruņurupucis')
t.pencolor=("blue")

t.color('white', 'red')
t.begin_fill()

for i in range(3):
    t.left(90)
    t.forward(100)
t.end_fill()

t.up
t.forward(150)
t.down

t.color('white', 'red')
t.begin_fill()

for i in range(3):
    t.left(90)
    t.forward(100)
t.end_fill()


t.done()