#Tuple: Is a collection of elements of any python data type
#Tuple vs List:
#1. syntax: you have to store the values in a tuple with (), but in list with []
#2. Tuple is immutable (Cannot change the value in tuple) but lists are mutable

#tuple declaration
marks = (100, 200, 300)
employeeData = ("Tom", 25, 'm', 23.33, True)

print(employeeData)  #output: ('Tom', 25, 'm', 23.33, True)

print(employeeData[0]) #output: Tom

#print(employeeData[5])  #output: IndexError: tuple index out of range

#backward indexing
print(employeeData[-4])  #output: 25


list = [10, 20, 30, 40]  #list is mutable, i.e, values can be changed
list[1] = 100
print(list)   #output: [10, 100, 30, 40]


#names = ("Java", "Python", "C")  #Immutable: cannot change values
# names[2] = "Dot net"
# print(names)         #output: TypeError: 'tuple' object does not support item assignment

# names = ("Java", "Python", "C")
# del names      #del deletes the tuple
# print(names)

#Concatenation of tuples
t1 = (1,2,3)
t2 = (1,2,1)

print(t1+t2)   #output: (1, 2, 3, 1, 2, 1)

t3 = (1,2,3)
print(t3*3)   #output:  (1, 2, 3, 1, 2, 3, 1, 2, 3)

#range slice:
t4 = (1,2,3,4,6)
print(t4[1:3])   #output: (2, 3)

#in: is a keyword
employeeData1 = ("Tom", 25, 'm', 23.33, True)
print(25 in employeeData1)  #output: True
print(35 in employeeData1)  #output: False

#not in:
print(35 not in employeeData1)  #output: True

#len:
length = len(employeeData1)
print(length)    #output: 5

#max number:
number = (12, 14, 50, 100)
print(max(number))   #output: 100

names1 = ("Java", "Python", "C")
print(max(names1))   #output: Python  (Verifies in alphabetic order and return the max value)
print(min(names1))   #output: C