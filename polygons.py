#Name: Paramveer Singh Bhele
#U-Number: U82076898
#Description: Drawing polygons with the turtle module - Assignment 3 - Used the numinput method of the turtle module to input the number of sides and the length of each side.
#The angle of each side of the polygon is calculated from the formula given in the question
#Used for loop and turtle functions for drawing the polygon. Length provided will be used for the turtle to move forward and angle calculated for turning the turtle.
#Then I have used if and elif to label the polygon drawn using the write method. I have referred from the turtle module on the official python site and used these methods.
#----------------------------------------------------------------------------------------------------------------------
import turtle
sides=int(turtle.numinput("Side entry", "Enter the number of sides:", default=3, minval=3, maxval=12))
length=int(turtle.numinput("Length entry", "Enter the length of each side:", default=50, minval=50, maxval=250))
angle=180-((180*(sides-2))/sides)
for i in range(sides):
    turtle.forward(length)
    turtle.right(angle)
if sides==3:
    turtle.write("Triangle", font=('Arial', 20, 'normal'))
elif sides==4:
    turtle.write("Square/Quadilateral", font=('Arial', 20, 'normal'))
elif sides==5:
    turtle.write("Pentagon", font=('Arial', 20, 'normal'))
elif sides==6:
    turtle.write("Hexagon", font=('Arial', 20, 'normal'))
elif sides==7:
    turtle.write("Heptagon", font=('Arial', 20, 'normal'))
elif sides==8:
    turtle.write("Octagon", font=('Arial', 20, 'normal'))
elif sides==9:
    turtle.write("Nonagon", font=('Arial', 20, 'normal'))
elif sides==10:
    turtle.write("Decagon", font=('Arial', 20, 'normal'))
elif sides==11:
    turtle.write("Hendecagon", font=('Arial', 20, 'normal'))
elif sides==12:
    turtle.write("Dodecagon", font=('Arial', 20, 'normal'))

turtle.exitonclick()

