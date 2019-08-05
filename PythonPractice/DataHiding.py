class Employee:

    #hidden data member or private member of Employee class
    __salary = 1000 #To define private variable OR hide variable we should __ (double underscore)

e1 = Employee()
# print(e1.__salary)  #this is not the right way of accessing hidden / private variable
'''
output:
AttributeError: 'Employee' object has no attribute '__salary'
'''

#Access private / hidden variable by using tricky syntax:
print(e1._Employee__salary)  #output: 1000

