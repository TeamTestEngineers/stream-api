class vector2D:
    x=0.0
    y=0.0

    def set(self,x,y):
        self.x = x
        self.y = y

def Main():
    vec = vector2D()
    vec.set(5,6)
    print("X: "+ str(vec.x)+", Y: "+ str(vec.y))

if __name__ == '__main__':
    Main()
    