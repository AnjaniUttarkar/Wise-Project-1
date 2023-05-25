import tkinter as tk
import turtle
import random
from random import randint
#import turtle
from time import sleep
# from tk import *
from _tkinter import *
from playsound import playsound
import winsound

tur=turtle.Screen()
#playsound('bee_audio.mp3')
screen=tur.getcanvas().winfo_toplevel()
#winsound.PlaySound('bee_audio.wav',winsound.SND_ASYNC)
#def play():


tur.bgpic("Untitled.gif")
screen.attributes("-fullscreen",True)

winsound.PlaySound('cocomelon.wav',winsound.SND_ASYNC)
n1 = int(turtle.textinput("Cell Details","Enter the first cell no: "))#int(input("Enter the first cell no: "))
tur.tracer(1) 
winsound.PlaySound('cocomelon.wav',winsound.SND_ASYNC)
n2 = int(turtle.textinput("Cell Details","Enter the second cell no: "))#int(input("Enter the second cell no: "))


if n1 > n2:
    n1, n2 = n2, n1

n1x, n1y, n2x, n2y, x, y, k = 0, 0, 0, 0, 0, 0, 1


for i in range(1, n2):
    y -= 2
    k += 1
    if k == n1:
        n1x, n1y = x, y
    if k == n2:
        n2x, n2y = x, y
    for j in range(i - 1):
        x -= 1
        y -= 1
        k += 1
        if k == n1:
            n1x, n1y = x, y
        if k == n2:
            n2x, n2y = x, y
    for j in range(i):
        x -= 1
        y += 1
        k += 1
        if k == n1:
            n1x, n1y = x, y
        if k == n2:
            n2x, n2y = x, y
    for j in range(i):
        y += 2
        k += 1
        if k == n1:
            n1x, n1y = x, y
        if k == n2:
            n2x, n2y = x, y
    for j in range(i):
        x += 1
        y += 1
        k += 1
        if k == n1:
            n1x, n1y = x, y
        if k == n2:
            n2x, n2y = x, y
    for j in range(i):
        x += 1
        y -= 1
        k += 1
        if k == n1:
            n1x, n1y = x, y
        if k == n2:
            n2x, n2y = x, y
    for j in range(i):
        y -= 2
        k += 1
        if k == n1:
            n1x, n1y = x, y
        if k == n2:
            n2x, n2y = x, y

#print(n1)#, n1x, n1y)
#print(n2)#, n2x, n2y)

a = abs(n1x - n2x)
b = abs(n1y - n2y)
c = 0

while a > 0 or b > 0:
    if b > a:
        b -= 2
    else:
        a -= 1
        b -= 1

    c += 1
print(c)
t= turtle.Turtle()

t.hideturtle()

t.penup()
t.goto(150,10)
winsound.PlaySound('abstract.wav',winsound.SND_ASYNC)
t.write(f"The distance between the two cells is {c}",align='center',font=('Times New Roman',45,'bold'))
#int(turtle.textinput("Output Dialog","The distance between the two cells is "))
#tur.write(c,align="center",font=('Times New Roman',12,'bold')

sleep(5)
tur.clear()

def next_screen(x,y):
    
    #tur.bgpic("next_screen.gif")
    button.hideturtle()
    #button.bgcolor("yellow")

button = turtle.Turtle()
turtle.Screen().bgcolor('bisque1')
button.hideturtle()
button.penup()
button.goto(0,-300)
#button.write("NEXT",align="center",font=("Arial",12,'bold'))


turtle.onscreenclick(next_screen)



import part3
