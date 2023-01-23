#Name: Paramveer Singh Bhele
#U-Number: U82076898
#Description: Area of a Flower - Assignment 1 Radius of circle is half of the radius entered by the user. Square has the same side as the radius. 
#----------------------------------------------
pi = 3.14159
radius = float(input("Enter the radius of the flower: "))
circles= 2*(pi*(radius/2)*(radius/2))
square= radius*radius#radius is same as side
final= square+circles
print("The area of the flower is ",final," square units.")







