#Week 5 Lecture 2 COP2510-2

#recap of break on nested structures
i = 1
while i<15:
    if i==7:
        break
    print(f"{i}")
    i += 2 

i = 1
while i<15:
    if i==7:
        if i==11:
            break
    print(f"{i}")
    i += 2 

#while loop and walrus operators
while(number:=int(input('Enter a positive number: ')))<0:
    number = int(input('Invalid entry - enter a positive number: '))
print(f'Your number is {number}')

#more about the turtle module
import turtle

#text input
name = turtle.textinput('Text input Box','Enter name')
print(name)

#numerical input
radius = turtle.numinput('Radius Entry Box','Enter radius',default=50,minval=10,maxval=300)
turtle.circle(radius)

#adjust speed
turtle.speed(0) #10 is the fastest, slow is 1

turtle.circle(100.125)
turtle.circle(100)

#clear screen
turtle.clearscreen()

#example of a problem
from turtle import *
color('red','yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos())<1:
        break
end_fill()
done()

#example
for n in range(4):
    turtle.fd(150)
    turtle.dot(10,'green')
    turtle.right(90)

turtle.clearscreen()

#adjust shape
turtle.shape("turtle")
turtle.shape("square")

#draw multiple shapes
x,y = -300,0
turtle.penup()
turtle.setpos(x,y)

for z in range(8):
    turtle.pendown()
    turtle.circle(40)
    x += 80
    turtle.penup()
    turtle.setpost(x,y)
    
#example
turtle.clearscreen()
num_cir = 36
angle = 10
speeD = 20

turtle.speed(speeD)
shape = turtle.textinput('Shape selection','Enter shape')
turtle.shape(shape)
radius = turtle.numinput('Radius Entry Box','Enter radius',default=50,minval=10,maxval=300)

for c in range(num_cir):
    turtle.circle(radius)
    turtle.left(angle)

#intro to functions
#void function
def fun1():
    print("this output statement is in a void function.")

#value returning function
def tripval(y):
    print(f"the value obtained was {y}")
    y*=3
    return y

#main portion
fun1() #calling the function

a = int(input('Etner a number: '))
a = tripval(a)
print(f'The value tripled is {a}')

