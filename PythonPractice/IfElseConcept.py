x = int(input("please enter the value of x"))

if x<0:
    print("x is negative number")
elif x>0:
    print("x is positive number")
elif x==0:
    print("x is neutral")
else:
    print("x is not defined")

#example of dead code
if True:
    print("PASS")
else:
    print("FAIL")

if 10>5:
    print("Hi")

#WAP to find out the highest number
a=100
b=200
c=300

if a>b and a>c:
    print("a is the highest number")
elif b>c:
    print("b is the highest number")
else:
    print("c is the highestr number")

total = int(input("enter the total value:"))
if total<100:
    total = total+20
elif total>100 and total<500:
    total = total+50
else:
    total = total + 100

print(total)
print("total=" + str(total)) #In python string to integer concatenation is not allowed, so use str() method
print(f'{"total value ="} {total}') #f strings in python