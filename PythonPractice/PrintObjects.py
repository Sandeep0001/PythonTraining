#String representation of class object:
#Object printing concept:

class Test:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    # def __repr__(self):  #representation method
    #     return "a:%s b:%s" %(self.x, self.y)

    # def __str__(self):    #string method
    #     return "value of a is %s and b is %s" %(self.x,self.y)

#Test code:
t = Test(10,20)  #Object creation
print(t)

'''
Ouput:
value of a is 10 and b is 20  #if string method is defined object will __str__ method to print the result
a:10 b:20                     #if __str__ is not defined then object will call __repr__ method
<__main__.Test object at 0x000000C9DA446390>  #if __repr__ and __str__ methods are not defined then it will print object address
'''