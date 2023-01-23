#Name: Paramveer Singh Bhele
#U-Number: U82076898
#Description: Rows of Grapevines - Assignment 1 Length of row, amount of space and the space between each vine is taken as an input from the user. Formula is then used to find out the how many vines can fit.
#-----------------------------------------------
Row= int(input('Enter the length of the row, in feet: '))
Espace=float(input('Enter the amount of space, in feet, used by an end-post assembly: ')) 
space=int(input('Enter the distance, in feet, between each vine: '))
Vnum= Row-(2*Espace)/space
print(f"You have enough space for {Vnum:.1f} vines")
