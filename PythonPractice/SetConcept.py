#Set: is not order based
#it stores different type of data like list and tuple
#it performs different mathematical operations
#does not store duplicate elements
#define a set: use {}

s1 = {100, "Tom", 12.33, True}
s2 = {1,1,2,2,3,3,}
print(s2)               #Output: {1, 2, 3}
print(s1)               #Output:  {True, 100, 'Tom', 12.33}

#set() function:
s3 = set("python")
print(s3)               #Output: {'t', 'n', 'h', 'y', 'o', 'p'}

s4 = set([10,20,30,40])  #storing list in set function
print(s4)              #output: {40, 10, 20, 30}

s5 = set((10,20,30,50))  #storing tuple in set function
print(s5)                #output: {10, 20, 50, 30}

#while creating a set object, you can store only Numbers, strings, tuple
#list and dictionary objects are not allowed

set1 = {(10,20), 30, 40}
print(set1)          #output: {40, (10, 20), 30}

# set2 = {[10,20], 30}
# print(set2)            #output: TypeError: unhashable type: 'list'

#set operations:
#union:  use | operator  OR union()
p1 = {1,2,3,4,5}
p2 = {5,6,7,8,9}
print(p1|p2)         #output: {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(p1.union(p2))  #output: {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(p2.union(p1))  #output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

#intersection: use & operator OR intersection()
p3 = {1,2,3,4,5}
p4 = {5,6,7,8,9}
print(p3&p4)         #output: {5}
print(p3.intersection(p4))  #output: {5}

#difference of sets: - operator OR difference()
p5 = {1,2,3,4,5}
p6 = {5,6,7,8,9}
print(p5-p6)         #output: {1, 2, 3, 4}
print(p6-p5)         #output: {8, 9, 6, 7}
print(p6.difference(p5))  #output: {8, 9, 6, 7}

#symmetric difference: ^
p7 = {1,2,3,4,5}
p8 = {5,6,7,8,9}
print(p7^p8)      #output: {1, 2, 3, 4, 6, 7, 8, 9}
print(p7.symmetric_difference(p8)) #output: {1, 2, 3, 4, 6, 7, 8, 9}

#set - In built methods:
#1. add():

s1 = {"Java", "Python", "C"}
s1.add("Perl")
print(s1)         #output: {'Perl', 'C', 'Python', 'Java'}

#2.update():
s2 = {"Java", "Python", "C"}
s2.update(["perl", "ruby"])    #updating using list
print(s2)         #output: {'C', 'Java', 'ruby', 'Python', 'perl'}

s2.update(("JS", "C++"))   #updating using tuple
print(s2)       #output: {'perl', 'ruby', 'Java', 'C', 'Python', 'C++', 'JS'}


#3. clear():
s2.clear()
print(s2)    #output: set()

#4. copy():
lang = {"Java", "Python", "C"}
lang1 = lang.copy()
print(lang1)    #ouptut: {'Java', 'C', 'Python'}

#5. discard():
lang = {"Java", "Python", "C"}
lang.discard("C")
print(lang)        #ouptput: {'Python', 'Java'}
lang.discard("Sandeep")
print(lang)             #ouptput: {'Python', 'Java'}

#6. remove():
student = {"Tom", "steve", "Peter"}
student.remove("Tom")
print(student)       #output: {'steve', 'Peter'}
# student.remove("Symond")
# print(student)     #output: KeyError: 'Symond'