#COP 2510 WEEK 9 LEC 1
name="Schinnel Small"

#use len to get the size of string(container)
print(f'The name "{name}" has {len(name)} characters.')

#string slicing
subname=name[0:5]#0 inclusive; 5 exclusive
print(subname)

#-ve indices can be used to access the ending characters
print(name[-3])
print(name[-5:-2])
name2=name+''
print(name2[-6:-1])
print(name[0:10:2])

#the lines below refer to the same character in the string
print(name[13])
print(name[-1])

#---------------nested lists--------------------
names=['John','jane','Jake','Jake',[11,5],'Jennifer']
print(names[0][1])#0 - 'John',1-'o'
print(names[-2][0])

#-----------useful methods for lists-------------
names.insert(2,'bob')#specify where values should be added with the index
names.insert(4,'kyle')
print(names)
names.append('john')#append can add nested lists
print(names)

#to remove values, use remove or pop
names.remove('John')
print(names)

names.pop() #by default, last element is removed
names.pop() #can specify index
print(names)

#--------list comprehension------------
#create a new list by modifying the original list
list1=[1,2,3,4,5]

list2=[j*5 for j in list1]#operation for range variables in original list

print(f'List1:{list1}')
print(f'list2:{list2}')

#you can use list comprehension with conditional (ternary form)
list3=[k-3 if k>3 else k+2 for k in list1]#note ternary form is first
print(f'List3:{list3}')

#use list comprehension with an if statement
list4=[m*4 for m in list1 if m<=3]
print(f'List 4:{list4}')

#you can use input statements too but....
list5=[int(input()) for n in list4]
print(f'List5:{list5}')
