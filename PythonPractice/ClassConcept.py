class Car:

    #class variables
    wheels = 4

    #Constructor of this class:
    def __init__(self):
        print("default construcor")


    def __init__(self, color):  #__init__ method is used for defining the constructor
        print("Car class constructor")
        self.color = color


    def test(self):  #self is same as this keyworkd in Java, in python it is mandatory to define self in a method
        print("test method")

    #any variable is declared inside the method or constructor: instance variable
    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price


#how to create an object of this class:

c1 = Car("Green") #output: Car class constructor
print(c1.wheels) #output: 4
print(Car.wheels) #output: 4 #In python we don't have concept of static and non static

c1.test()  #Output: test method
c1.setPrice(1000)
print(c1.getPrice()) #output: 1000


#c2 = Car()  #Constructor overloading is not allowed in python, python will always consider latest constructor
'''
output:
c2 = Car()
TypeError: __init__() missing 1 required positional argument: 'color'
'''

class Test:
    a = 10

#blank class: representation
class Pop:
    pass

p1 = Pop()