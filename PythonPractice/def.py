def fun():
    S = 0
    for i in range(10):
        S += 1
    return S

print(fun())

def fun1():
    m = 0
    for j in range(10):
        m += j
        yield m

for i in fun1():
    print(i)