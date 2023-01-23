#Name: Paramveer Singh Bhele
#U-Number: U82076898
#Description: Ratio of Volume of Spheres vs Containers - Assignment 1 Program inputs the numbers of spheres and the diameter of a sphere. Then the height and volumes of the sphere and the cylinder are calculated. Finally, the percentage of area occupied by the spheres is computed. 
#----------------------------------------------------------------------
import math
num_s= int(input("Enter the number of spheres to be placed in the container: "))
dia=float(input("Enter the diameter of each sphere (in inches): "))
height= dia*num_s
print(f"The container would need to be at least {height} inches to hold the {num_s} spheres. ")
rad=dia/2
vol_s=num_s*((4/3)*math.pi*(rad**3))
vol_c=math.pi*(rad**2)*height
vol=(vol_s/vol_c)*100
print(f"The {num_s} spheres will occupy {vol:.2f}% of the container. ")