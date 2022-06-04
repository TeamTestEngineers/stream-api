class person(object):
    def __init__(self,name):
        self.__name=name
    
    def getName(self):
        return self.__name

    def isEmployee(self):
        return False

class Employee(person):
    
    def __init__(self, name):
        super().__init__(name)
        
    def isEmployer(self):
        print('this is the Employee class')
    
x = Employee('Rakesh')
print(x.isEmployee())
x.isEmployer()
print(x.getName())

y= person('Roger')
print(y.getName())
print(y.isEmployee())
#print(y.__name)
