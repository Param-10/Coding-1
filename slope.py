#Name: Paramveer Singh Bhele
#U-Number: U82076898
#Description: Slope of a line - Assignment 1 The program inputs two points in a single line and then uses the slope formula to find the slope between the two points.
#-----------------------------------------------
x1,y1=input("Enter the coordinates of the first point: ").split()
x1=float(x1)
y1=float(y1)
x2,y2=input("Enter the coordinates of the second point: ").split()
x2=float(x2)
y2=float(y2)
slope=(y2-y1)/(x2-x1)
print(f"The slope of the line that connects two points ({x1},{y1}) and ({x2},{y2}) is {slope:.3f}")
