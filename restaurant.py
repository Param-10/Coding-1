#Name: Paramveer Singh Bhele
#U-Number: U82076898
#Description: Restaurant Selector - Assignment 2 : Take the inputs from the user. 
#Converted the input entered by the user to lowercase, therefore the values entered are not limited by uppercase or lowercase.
#Then used elif to find compare the inputs and then show the correct output according to the values entered.
#2^3 = 8. 8 is the number of possible outputs for the question. Incase wrong values are entered then the else statement tells the user to enter correct values.
veg=input('Is anyone in your party vegetarian?')
veg=veg.lower()
vegan=input('Is anyone in your party vegan?')
vegan=vegan.lower()
glu=input('Is anyone in your party gluten free?')
glu=glu.lower()

print('Here\'s your restaurant choices:')


if veg=='no' and vegan=='no' and glu=='no':
    {print('Fleming\'s Prime Steakhouse\n'
           'Bella\'s Italian Restaurant\n'
           'Gourmet Pizza Company\n'
           'True Food Kitchen')}
    

elif veg=='yes' and vegan=='no'and glu=='yes':
    {print('Gourmet Pizza Company\n'
           'True Food Kitchen')}
    

elif veg=='yes' and vegan=='no'and glu=='no':
    {print('Bella\'s Italian Restaurant\n'
           'Gourmet Pizza Company\n'
           'True Food Kitchen')}
    

elif veg=='yes' and vegan=='yes' and glu=='yes':
    {print('True Food Kitchen')}


elif veg=='no' and vegan=='no' and glu=='yes':
    {print('True Food Kitchen\n'
           'Gourmet Pizza Company')}


elif veg=='no' and vegan=='yes' and glu=='no':
    {print('True Food Kitchen')}


elif veg=='yes' and vegan=='yes' and glu=='no':
    {print('True Food Kitchen')}


elif veg=='no' and vegan=='yes' and glu=='yes':
    {print('True Food Kitchen')}


else:
    {print("Enter yes/no and try again.")}