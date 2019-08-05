#While loop

count = 0
while count<3:
    print("Hello world")
    count = count + 1

print("-------------------------------------------")

#While loop with else
num = 0
while num<3:
    print("Hello Python")
    num = num + 1
else:
    print("Bye Python")

print("-------------------------------------------")

#for loop

name = ["java", "python", "dot net", "c sharp"]
for i in name:
    print(i)

print("-------------------------------------------")

str = "I love Python"
for i in str:
    print(i)

print("-------------------------------------------")

list = ["Naveen", "Automation", "Labs"]
for index in range(len(list)):
    print(list[index])

print("-------------------------------------------")

#for loop with else
CountryList = ["India", "UK", "USA", "Germany"]
for index in range(len(CountryList)):
    print(CountryList[index])
else:
    print("CountryList is over")

print("-------------------------------------------")

CityList = ["Bangalore", "Mysore", "Boston", "Ny"]
for index in range(4):
    print(CityList[index])
else:
    print("CityList is over")

print("-------------------------------------------")
#nested for loop
for i in range(1,5):
    for j in range(i):
        print(i, end='')
    print()

'''
output
1
22
333
4444
'''

print("-------------------------------------------")
for i in range(5):
    for j in range(i):
        print(i, end='')
    print(i)

'''output
0
11
222
3333
44444
''' s