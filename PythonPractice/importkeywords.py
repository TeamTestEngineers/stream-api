import keyword

print('The list of kwywords in :')
j=1
for i in keyword.kwlist:
    print(j,' ',i)
    j += 1


#True False and None keyword
print (False == 0)
print (False == 1)
print (True + True + True)
print (True + False + False)
print (None == 0)
print (None == [])
print (True or False)


if 's' in 'geeksforgeeks':
    print('s is part of geeks for geeks')
else:
    print('s is not part of geeks for geeks')

for i in 'geeksfrgeeks':
    print(i, end=" ")


print("\r")

print(' ' is ' ')

print([] is [])

print({} is {})




