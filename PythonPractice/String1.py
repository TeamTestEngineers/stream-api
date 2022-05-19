from msilib.schema import ReserveCost


String1 = 'Welcome to the Geeks World'
print ('String with the use of single quotes: ')
print (String1)

String1="I'm a Geek"
print("\nString with the use of Doubel Quotes: ")
print(String1)

String1 = '''
    geeks
        for
            geeks
                '''
print("\n String with the use of triple Quotes: ")
print(String1)

String1='geeksforgeeks'
print('Initial String')
print(String1)

print('\n First characters of string is: ')
print(String1[0])

print('\n Last characters of String is: ')
print(String1[-1])

# string slicing
print("\n Slicing characters from 3-12: ")
print(String1[3:12])

print("\n Slicing characters between "+
        "3rd and 2nd last characters: ")
print(String1[3:-2])

#updating a entire string

string1 = "Hello, I'm a geek"
print("Initial String:")
print(string1)

String = "Welcome to the geek world"
print("\n Updated String")
#updation of a character
#you cannot update a char or delete a char because String is immuatbel

#String1[2]='u'
#print('\n updating character at 2nd Index: ')
#print(String1)

#Escape Sequenceing in python 
String1 = '''
    I'm a Geek'''

#Escaping Doubel Quotes
String1= "I'm a \"geek\""

inputSentence = input("PLase Input a sentence : ")
print(" ". join(reversed(inputSentence.split())))

