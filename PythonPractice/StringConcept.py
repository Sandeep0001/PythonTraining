s1 = "test selenium"
s2 = 'hello world'

print(s1)
print(s2)

print(s1[0])
#print(s1[13]) #string index out of range

print(s1+" "+s2)

print("hello \n world")
print("hello \t world")

print("test" in s1)
print("java" not in s1)

print("my name is %s and my age is %d" %("Tom", 25)) #python supports formating operator

s3 = """test java
test pyhton
test selenium
test robot framework"""

print(s3)

s4 = '''hi
pyhon is cool'''

print(s4)

#string literals
print('hi i\'m python')
print("hi \"python\"")

str = "this is my Python code and I love Python"
print(str)
print(str.capitalize()) #capitalize() will convert first letter into capital letter

print(str.count("Python")) #counts the number of occurance

print(str.find("code")) #finds the location of the word i.e 18
print(str.find("java")) #resturns -1 as the word java is not available in the provided string

print(len(str)) #returns the length of the string
print(str.lower()) #whole string will be printed in lower format

#trimming up the spaces
str1 = "   hello   "
print(str1.lstrip()) #lstrip() method will remove left hand spaces of string
print(str1.rstrip()) #rstrip() method will remove right hand spaces of string

str2 = "abz"
print(max(str2)) #returns the maximum alphabet available in the string i.e it returns z
print(min(str2)) #returns the minimun alphabet available in the string i.e, it returns a

str3 = "hello test python"
print(str3.replace("hello", "Bye"))  #replace() method replaces the string

str4 = "java hello python hello javascript"
str5 = str4.split("hello") #split() method returns array so store in some variable output(['java', 'python', 'javascript'])

print(str5)
print(str5[0]) # returns the first index of an array i.e, java

print(str4.upper())


st = "Python"
print(st[0]) #prints P
print(st[5]) #prints n
print(st[-1]) #prints n
print(st[-6]) #prints P

a = "test"
b = "test"

print(a is b) #checks the identity #return true
print(a==b) #checks the value  #returns true

s1 = "test selenium"
s2 = 'hello world'

print(s1)
print(s2)

print(s1[0]) #t
#print(s1[13]) #String index out of range

print(s1+ " " + s2) #Concatenation

print("hello \n world") #prints world in new line
print("hello \t world") #prints world in tab space

print("test"*5)

print(s1[0:5]) #test is the output (range)

#in operator
print("test" in  s1) # output is true
print("java" in  s1) # output is false
print("java" not in s1) #output is true

#formatting operator
print("my name is %s and my age is %d" %("Tom", 25))

#triple single quote string
s3 = '''test java
test python
test selenium
in python code'''

#triple double quote string
s4 = """hi this is my python code
and I am learning python
and I am so happy"""
print(s4)
