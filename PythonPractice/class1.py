class dog:
    # A simple class
    # attribute
    attr1 = "mammal"
    attr2 = "dog"


# A sample Method
    def fun(self):
        print("I'm a ", self.attr1)
        print("I'm a ", self.attr2)
        # print(attr1)
        # print(attr2)

# Driver code
# object initialization

Rodger = dog()
print(Rodger.attr1)
print(Rodger.attr2)
Rodger.fun()
