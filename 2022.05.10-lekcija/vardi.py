import turtle as t
import random

t.tracer(0)
t.hideturtle()

green="#7aa86a"
yellow="#c6b567"
gray="#787c7f"
# gray="787c7f"

vardi=open('vardi.txt').read().split('\n')
atbilde=random.choice(vardi).upper()

minejums=""
mineju_skaits=0

def draw_box(x,y,text,color):
    t.setheading(0)
    t.up();t.goto(x,y);t.down()
    

    t.pencolor('gray')
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(50)
        t.right(90)
    t.end_fill()
    t.up()

    t.goto(x+27,y-46)
    t.pencolor('white')
    t.write(text,align='center',font=('Arial',25,'bold'))



def draw_board():
    for i in range(6):
        for j in range(5):
            draw_box(-145+60*j,175-60*i,'','white')
    t.update()

def iekrasot(minejums,atbilde):
    vienadi_burti={burts:0 for burts in atbilde}
    for i in range(5):
        if minejums[i]==atbilde[i]:
            draw_box(-145+60*i,175-60*mineju_skaits,minejums[i],green)
            vienadi_burti[minejums[i]]+=1

    for i in range(5):
        if minejums[i]==atbilde[i]:
            continue
        elif minejums[i] not in atbilde:
            draw_box(-145+60*i,175-60*mineju_skaits,minejums[i],gray)
        elif vienadi_burti[minejums[i]]==atbilde.count(minejums[i]):
            draw_box(-145+60*i,175-60*mineju_skaits,minejums[i],gray)
        else:
            draw_box(-145+60*i,175-60*mineju_skaits,minejums[i],yellow)
            vienadi_burti[minejums[i]]+=1

draw_board()

while True:
    minejums=t.textinput('Ievade','Mini 5 burtu vārdu: ').upper()

    if len(minejums)!=5 or not minejums.isalpha():
        continue

    iekrasot(minejums,atbilde)
    mineju_skaits+=1
    if minejums==atbilde:
        t.textinput('Uzvara!','Tu uzvarēji!')
    elif mineju_skaits==6:
        # t.textinput('Zaudējums!','Tu zaudējis!Pareiza atbilde bija: '+ atbilde+'!')
        break

# t.done()