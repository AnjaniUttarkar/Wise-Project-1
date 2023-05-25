import tkinter as tk
import turtle
import random
from random import randint
import turtle
from time import sleep
# from tk import *
from _tkinter import *
#from playsound import playsound
from playsound import playsound
import winsound

winsound.PlaySound('bee_sound.wav',winsound.SND_ASYNC)
turtle.Screen().setup(width=0.5,height=0.75)
size = 30
circles = 100
#playsound('bee_audio.mp3')
turtle.speed('fastest')

turtle.colormode(255)

def move(length, angle):
                turtle.right(angle)
                turtle.forward(length)
#num=1

def hex(num):
        turtle.pendown()
        turtle.color( randint(0,255),randint(0,255),randint(0,255) )
        turtle.begin_fill()
        for i in range(6):
                move(size,-60)
        turtle.end_fill()
        turtle.penup()
        turtle.color('white')
        turtle.write(num,align="center",font=('Times New Roman',12,'bold'))
        
# start
turtle.penup()
num=1

for circle in range (circles):
        if circle == 0:
                hex(num)
                num +=1
                move(size,-60)
                move(size,-60)
                move(size,-60)
                move(0,180)
        for i in range (6):
                move(0,60)
                for j in range (circle+1):
                        hex(num)
                        num=num+1
                        move(size,-60)
                        move(size,60)
                move(-size,0)
        move(-size,60)
        move(size,-120)
        move(0,60)
turtle.exitonclick()