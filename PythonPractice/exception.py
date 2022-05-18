a=4
b=0

try:
    k = a//b #raise divide by zero execption
    print(k)
except ZeroDivisionError:
    print("Can't divide by Zero")

finally:
    print('This is always executed')

# assert keyword
# using assert to check for 0
print("the value of a/b is: ")
assert b != 0, "Divide by 0 error"
print(a/b)