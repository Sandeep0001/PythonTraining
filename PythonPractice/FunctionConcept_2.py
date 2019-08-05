def login(username, password):
    print(username, password)

login("Sandeep", "1234") #output: Sandeep 1234

login(username="Sandeep", password="1234") #output: Sandeep 1234


# *args: different values in single variable
def getMarks(*arg):
    for x in arg:
        print(x)

getMarks(10,20,30,30,45)
'''
output:
10
20
30
30
45
'''

getMarks("A+", "B+", "B-")
'''
output:
A+
B+
B-
'''

#Keyword arguements : denoted by **args
def getStudentMarks(**args):
    for key, value in args.items():
        print("%s==%s" %(key, value))

getStudentMarks(naveen=10, sandeep=20)

'''
output:
naveen==10
sandeep==20
'''

getStudentMarks(key="apple", sellerName="Xeon")

'''
Output:
key==apple
sellerName==Xeon
'''

#lambda function: Annonymous function
#a function without any name is called lambda function

cube = lambda x: x*x*x

print(cube(4)) #output: 64

total = lambda marks: marks+30

print(total(100))  #output: 130