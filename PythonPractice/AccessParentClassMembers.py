class Base(object):

    def __init__(self, x):
        self.x = x

class Child(Base):

    def __init__(self, x, y):
        Base.x = x
        self.y = y

    def printWork(self):
        print(Base.x, self.y)


#Test Code
ob = Child(10, 20)
ob.printWork()    #output: 10 20

ob1 = Child(30, 40)
ob1.printWork()   #output 30 40