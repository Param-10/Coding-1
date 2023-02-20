#COP 2510 Section 2 week 7 lecture 1
from PIL import Image
#------funcition definitions-----
def main():
    print('Here are some popular games:')
    esportgames()

    #local dictionary{key:value}
    animals={'cat':'floof','bird':'birb','dog':'pupper','snake':'danger noodle'}

    #to access a specific value in a dictionary
    print(animals['dog'])

    #call a function that uses a dictionary
    rename(animals)

    #working with a image!
    image1=Image.open("/Users/paramveer/Pictures/Lightroom Saved Photos/IMAGE1.jpg")

    #display image(without using function)
    image1.show()

    #call image function
    showpic(image1)

    #create a thumbnail
    image2=Image.open('/Users/paramveer/Pictures/Lightroom Saved Photos/image2.jpg')
    image2.thumbnail((250,250))
    image2.save("minigw3.png")
    showpic(image2)

    #test function that returns a list
    value=int(input('what is the starting value?'))
    amt=int(input('how many multiples?'))

    valam=(value,amt)
    #valam=



    print(f'the first{amt} multiples of {value} are:\n{multiples(value,amt)}')




#--------end main---------
#coid function witt no parameters and a local list
def esportgames():
    #create local list
    games=['dota 2', 'fortnite','league of legends','counter strike']

    for(index, element) in enumerate(games):
        print(f'{index+1}.{element}')
    print()

    #to access a specific element:
    print(games[2])
    print()

    #print in reverse
    rank=4
    for i in reversed(games):
        print(f'{rank}.{i}')
        rank-=1
    print()
#------end esportgames-----------

#void function that accepts a dictionary as a parameter
def rename(ani):#ani to be a dictionary
    for k in ani:
        print(f'animal:{k}\t\t Alternate name:{ani[k]}')

#-------end rename-----------

#function that accepts an image
def showpic(img):#img to be an image object
    img.show()

def multiples(v,a):
    mult=[]
    for i in range(1,a+1):
        mult.append(i*v)#append - add values to the end of the list
    return mult

def multiples2(va):#va to be a tuple
    mult=[]
    for i in range(1,va):
        mult.append(i*va[0])#append - add values to the end of the list
    return mult


#------no function definitions below this line---------
main()