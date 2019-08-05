#def should be used to define the function
#zero parametrized function
def test():
    print("Hey I am function")

test() #Output: Hey I am function

#Single parametrized function
def abc(a):
    print(a+10)

abc(10)  #output: 20

#optional / default paramterized function
def getCountryName(name="India"):
    print(name)

getCountryName()        #output: India
getCountryName("USA")   #output: USA

#pass a list to a function
def getNames(list):
    for x in list:
        print(x)

names = ["Java", "Python", "C"]
getNames(names)
'''
Output:
Java
Python
C'''

#function with return
def sum(a,b):
    return a+b

x = sum(10, 20)
print(x)  #Output: 30

def getCapitalName(countryName):
    if countryName == "India":
        print("New Delhi")
    elif countryName == "USA":
        return "Washington DC"

print(getCapitalName("USA"))  #Output: Washington DC
getCapitalName("India")       #Output: New Delhi


def launchBrowser(browserName):
    if browserName == "chrome":
        print("launch browser google chrome")
    elif browserName == "firefox":
        print("launch firefox browser")
    else:
        print("browser not defined")

launchBrowser("chrome")  #launch browser google chrome

#Recursion in python : recursion means a function calling itself
#WAP to get  a factorial of given number
#fact(4) = 4*3*2*1 = 24

def fact(num):
    if num>1:
        num = num*fact(num-1)
    return num

print(fact(4))  #output: 24


def login(username, password):
    print("login with %s and %s" %(username,password))

login("Sandeep", "1234")  #output: login with Sandeep and 1234