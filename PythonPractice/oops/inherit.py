class pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class dog(pet):
    def __init__(self,name,age):
        super().__init__(name,age)

def Main():

    p = pet('pet',1)
    d = dog('dog',2)

    print("is p a dog? ", str(isinstance(p,dog)))
    print("is p a pet? ", str(isinstance(p,pet)))
    print("is d a dog? ", str(isinstance(d,dog)))
    print("is d a pet? ", str(isinstance(d,pet)))

if __name__ == '__main__':
    Main()