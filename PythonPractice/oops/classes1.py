class myclasses:
    number = 0
    name = "noname"

def Main():
    me = myclasses()
    me.number = 1337
    me.name = "Harrssh"

    print(me.name +" "+str(me.number))

if __name__ =='__main__':
    Main()

