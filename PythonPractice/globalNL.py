#global variable
a=15
b=20

def add():
    c = a+b
    print(c)

add()

#nonlocal keyword
def fun():
    var1 = 10

    def gun():
        # tell python explicitley that it
        # has to access var1 initialized 
        # in fun on line 2
        # using the keyword nonlocal
        nonlocal var1

        var1 = var1 + 10
        print(var1)
    gun()
fun()