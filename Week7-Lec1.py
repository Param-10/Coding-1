#COP 2510 Section 2 week 7 lecture 1

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

#void function that accepts a dictionary as a parameter
def rename(ani):#ani to be a dictionary
    for k in ani:
        print(f'animal:{k}\t\t Alternate name:{ani[k]}')

#-------end rename-----------


#------no function definitions below this line---------
main()