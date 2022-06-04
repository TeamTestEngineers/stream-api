from ctypes import py_object


class employee():

    def __init__(self):
        print("Employee created")

    def __del__(self):
        print("Destructor called, Employee deleted")
    
    def inbetween(self):
        print("this is inbetween method")

obj = employee()
obj.inbetween()
