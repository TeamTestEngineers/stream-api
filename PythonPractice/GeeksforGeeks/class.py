class dog():
    def __init__(self,name,breed) -> None:
        self.name=name
        self.breed=breed
        
    
    def func(self,age):
        print('name of the dog {0}\nage of the dog {1}\nbreed of the dog {2}'\
              .format(self.name,self.breed,age))
            
class person():

    def __init__(self,name):
        self.age=6
        self.name=name

    def setSex(self,sex):
        self.sex=sex

    def getSex(self):
        return self.sex

class Addition():
    first=0
    second=0
    answer=0
    #parameterized constructur
    def __init__(self,f,s):
        self.first=f
        self.second=s
    
    def display(self):
        print("First Number= "+str(self.first))
        print("SecondNumber= "+str(self.second))
        print("Addition of two numbers = "+str(self.answer))

    def addition(self):
        self.answer=self.first+self.second

obj = Addition(1000,2000)
obj.addition()
obj.display()

x = dog('rocky','lab')
x.func(3)

y = person('Rakesh')
print(y.name,y.age)
y.setSex('male')
print(y.getSex())