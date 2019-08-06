class Person(object): #object is super class of all the classes, in python by default object is created

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False

class Employee(Person):  #inherting the Person class

    def isEmployee(self):  #Method overiding
        return True


#Test Person
emp = Person("Sandeep")
print(emp.name)                         #output: Sandeep
print(emp.getName(), emp.isEmployee())  #output: Sandeep False

emp1 = Employee("Tom")
print(emp1.name)                        #Output: Tom
print(emp1.getName())                   #Output: Tom
print(emp1.isEmployee())                #Output: True