class Base(object):
    pass  #Empty class

class Child(Base):
    pass  #Empty Class


#Test code:
print(issubclass(Child, Base))  #issubclass() method is used to verify the base class #Output: True
print(issubclass(Base, Child))  #Output: False

c = Child()
b = Base()

print(isinstance(b, Child))   #isinstance() method is used to verify the refernce variable of a class #Output: False
print(isinstance(c, Child))  #output: True
print(isinstance(c, Base))   #Output: True  #child class reference can be a instance of base class