#Multiple Inheritance is allowed in Python

class Base1(object):

    def __init__(self):
        self.str1 = "Sandeep"
        print("Base1")

class Base2(object):

    def __init__(self):
        self.str2 = "Tom"
        print("Base2")


class Child(Base1, Base2):  #Achieved multiple inheritance
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)

        print("Child")

    def printStrings(self):
        print(self.str1)
        print(self.str2)

ob = Child()    #this object will call the constructor
ob.printStrings()
'''
output:
Base1
Base2
Child
Sandeep
Tom
'''