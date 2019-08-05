score = [10,20,40,50,97]
print(score)

#Slicing feature
print(score[0]) #prints 10
print(score[-2]) # prints 50

#new / shallow copy of the list
print(score[:])

#List's concatenation
print(score + [1,2,3])
print(score + ["A", "B", "C"])

number = [1,2,3,4,5]
number[2] = 90 #replaces the second index value i.e lists are mutable
print(number)

#Append
print(number.append(100 ))

name = ['a', 'b', 'c', 'd', 'e']
print(name)
name[2:5] = ['C', 'E', 'D'] #replaces the indexes of the list for the given range
print(name)
name[2:5] = [] #replaces the range with null value
print(name)

name[:] = []
print(name)
name.append([1,2,3])
print(name)

test = [20,30,40,50,60]
print(len(test))

#nested lists:
a = ['a', 'b', 'c']
n = [1,2,3]
x = [a,n]
print(x) #output [['a', 'b', 'c'], [1, 2, 3]]
print(x[0]) #output ['a', 'b', 'c']
print(x[1]) #output [1, 2, 3]

print(x[0][1]) #output b
print(x[1][2]) #output 3
