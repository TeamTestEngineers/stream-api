#list in python are created by just placing a sequence of non-
# homogenous elements in square brackets. 

list=[]
print('Blank list')
print(list)

list=[10,20,30,40]
print('\nlist of numbers')
print(list)

list=['geeks',
'for','geeks']
print('\nlist of string')
print(list)

print('\nlist the individual items')
print(list[0])
print(list[2])

list=[['geeks','for'],['geeks']]
print('\nMulti-dimensilnal list')
print(list)

#Creattging a list with multiple distinct or duplicate elements
list=[1,2,4,4,3,3,3,6,5]
print('\nList with the use of dupkuicate numbers:')
print(list)

print(len(list))

list=[1,2,3,'geeks','for',5,6,7,'geeks']
print(list)
print(len(list))

#Adding Elements to list
list=[]
print('Initial blank list')
print(list)

list.append(10)
list.append(20)
list.append(30)
list.append(40)

print(list)

for i in range(50,90,10):
    list.append(i)
print(list)

#updating a list within another list

list2=['geeks','for']
list.append(list2)
print(list)

List=[1,2,3,4,5]
print("Initial List: ")
print(list)

print('\nList after performaing Insert Operations: ')
list.insert(3,13)
list.insert(0,'geeks')
print(list)

#using Extend method 
list=[1,2,3,4,5]

print("Inintial List: ")
print(list)

list.extend([8,'geeks','always'])
print(list)

#using remove Method:
list=[1,2,3,4,5,6,
7,8,9,0,101,1,1,2,2,3,4,]
print(list)
list.remove(5)
list.remove(6)
print(list)