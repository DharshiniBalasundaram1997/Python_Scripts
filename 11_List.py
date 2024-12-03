#List: It is datatype.
# It will store multiple items in variable
# List : Square Brackets
# Where the list is Ordered, Changeable and Allow Duplicates

l1 = ['a','b','c']
print(l1) #Result: ['a', 'b', 'c']
print(type(l1)) #Result:<class 'list'>

# Where the list is Ordered, Changeable and Allow Duplicates
# Lists are collection

l1 = ['a','b','c','a','b','c','a','b','c']
print(l1)
print(type(l1))
print(len(l1))


l1 = ['a','b','c'] #List can be only string
l2 = [1,2,6.0,10+8j,10]  #List can be integers/float/complex
l3 = [True,False,True,False] #List can be collection of boolean
l4 = ['a','b','c', 10,19.3,True,'d'] #List can be mixed data type

print(l1,l2,l3,l4, sep='\n')
#Result: ['a', 'b', 'c']
# [1, 2, 6.0, 8j, 10]
# [True, False, True, False]
# ['a', 'b', 'c', 10, 19.3, True, 'd']

print(type(l1),type(l2),type(l3),type(l4), sep="\n")
#Result:<class 'list'>
# <class 'list'>
# <class 'list'>
# <class 'list'>



#List – range function:
l1 = range(11)
print(l1) #Result:range(0, 11)


l1 = list(range(11)) #putting the range in list constructor
print(l1) #Result:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l2 = list(range(5,11)) #putting the range in list constructor
print(l2) #Result:[5, 6, 7, 8, 9, 10]

l3 = list(range(2,11,2))
print(l3) #Result:[2, 4, 6, 8, 10]


#List - Repetition:
l1 = list(range(6))
print(l1) #Result:[0, 1, 2, 3, 4, 5]

l2 = l1 * 3
print(l2) #Result:[0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]

print(sep="\n")
#or

l1 = list(range(6))
print(l1) #Result:[0, 1, 2, 3, 4, 5]

n = 3
l2 = l1 * n
print(l2) #Result:[0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]


#List - Repetition: Giving negative numbers
l1 = list(range(6))
print(l1) #Result: [0, 1, 2, 3, 4, 5]

n = -3
l2 = l1 * n
print(l2) #Result: []     =>it will give an empty array because of the -ve number
"""
from fileinput import lineno
from tokenize import endpats

from unicodedata import numeric

"""#List - Printing the values in empty list , o/p in pyramid format
l=[]
for i in list(range(5)):
  l.append(int(i))
  print(l)
print(sep="\n")
#Result: 
# [0]
# [0, 1]
# [0, 1, 2]
# [0, 1, 2, 3]
# [0, 1, 2, 3, 4]


#List - Printing the values in empty list, o/p in 1 line format
l=[]
for i in list(range(5)):
  l.append(int(i))
print(l)  #Result: [0, 1, 2, 3, 4]


#List - Pushing the values from one list to another list, o/p in pyramid format
l1 = [1,2,3]
l2 = []

for i in list(l1):
  l2.append(i)
  print(l2)

#List - Pushing the values from one list to another list, o/p in 1 line format
l1 = [1,2,3]
l2 = []

for i in list(l1):
  l2.append(i)
print(l2)


# List - Index
#Items in the list is Ordered
l1 = [10, 20, 30, 40, 50] #This list has 5 items and based on index it will work
print(l1)  #Result:[10, 20, 30, 40, 50]

#postivie index
print(l1[2]) #Result:30

# Negative index
l1 = [10, 20, 30, 40, 50]
print(l1[-2]) #Result:40


# List Slicing – Start -end
l1 = [10, 20, 30, 40, 50,60]
print(l1[1:5]) #Result:[20, 30, 40, 50]

l1 = [10, 20, 30, 40, 50,60]
print(l1[:5]) #Result:[10, 20, 30, 40, 50]
print(l1[1:]) #Result:[20, 30, 40, 50, 60]

# List Slicing – Start -end - step
l1 = [10, 20, 30, 40, 50,60]
print(l1[::2]) #Result:[10, 30, 50]

#I want to update the single item in the collection
l1 = [10, 20, 30, 40, 50,60]
print(l1) #Result:[10, 20, 30, 40, 50, 60]
l1[2] = ' Apples'
print(l1) #Result:[10, 20, ' Apples', 40, 50, 60]

#I want to update the multiple item in the collection
l1 = [10, 20, 30, 40, 50,60]
print(l1) #Result:[10, 20, 30, 40, 50, 60]

l1[1:4] = ['A','B','C']
print(l1) #Result:[10, 'A', 'B', 'C', 50, 60]

#or
l1 = [10, 20, 30, 40, 50,60]
print(l1) #Result:[10, 20, 30, 40, 50, 60]
l1[1:4] = 'A','B','C'
print(l1) #Result:[10, 'A', 'B', 'C', 50, 60]

#or
l1[1:4] = ['A','B','C','E','F']
print(l1) #Result:[10, 'A', 'B', 'C', 'E', 'F', 50, 60]

#or
l1[1:4] = ['A']
print(l1) #Result:[10, 'A', 'E', 'F', 50, 60]





#Items in the list is Changeable

#How to add the items in the list
l1 = [10, 20, 30, 40, 50,60]
print(l1)

print(dir(l1))


#append() - from the list
#append -> it will add the item at the end of the collection
l2 = [10, 20, 30, 40, 50,60]
l2.append('Orange')
print(l2) #Result:[10, 20, 30, 40, 50, 60, 'Orange']



#insert() -> (index, item) - from the list
l2 = [10, 20, 30, 40, 50,60]
l2.insert(2,'Mango')
print(l2) #Result:[10, 20, 'Mango', 30, 40, 50, 60]

#extend() -> (collection) - from the list
l1 = [10, 20, 30, 40, 50,60]
l2 = ["A","B","C"] #it is applicable for list l2 = ["A","B","C"], set=> l2 = ("A","B","C"), tuples => l2 = {"A","B","C"}
l1.extend(l2)
print(l1) #Result:[10, 20, 30, 40, 50, 60, 'A', 'B', 'C']

# If we try to use for number list, we can use concat or append
l1 = [1,2]
l2 = [3,4]
l3 = l1 + l2 #concat
print(l3) #Result:[1, 2, 3, 4]

# or we can use append
l1 = [1,2]
l2 = [3,4]
for x in l2:
    l1.append(x)
print(l1) #Result:[1, 2, 3, 4]


# remove() - from the list
l1 = [10, 20, 'Mango', 30, 40, 50, 60, 'Orange' , 'A' , 'B', 'C']
print(l1) #Result:[10, 20, 'Mango', 30, 40, 50, 60, 'Orange', 'A', 'B', 'C']

l1.remove(50)
print(l1) #Result:[10, 20, 'Mango', 30, 40, 60, 'Orange', 'A', 'B', 'C']

l1.remove('Mango')
print(l1) #Result:[10, 20, 30, 40, 60, 'Orange', 'A', 'B', 'C']


#pop- from the list
#pop will remove the items from the last
l1 = [10, 20, 'Mango', 30, 40, 50, 60, 'Orange' , 'A' , 'B', 'C']
l1.pop()
print(l1) #Result:[10, 20, 'Mango', 30, 40, 50, 60, 'Orange', 'A', 'B']

l1.pop(2)
print(l1) #Result:[10, 20, 30, 40, 50, 60, 'Orange', 'A', 'B']



#delete - from the list
#By mentioning the range(start and end) we can delete the particular items from the list
l1 = [10, 20, 'Mango', 30, 40, 50, 60, 'Orange' , 'A' , 'B', 'C']
del l1[1:3] #Result:[10, 30, 40, 50, 60, 'Orange', 'A', 'B', 'C']
print(l1)


#How to empty the entire list - clear() method:
l1 = [10, 20, 'Mango', 30, 40, 50, 60, 'Orange' , 'A' , 'B', 'C']
l1.clear()
print(l1) #Result:[]

#Index– in List:
l1 = ['Bananas', 'Papayas', 'Cherries', 'Apples' ]
print(l1) #Result:['Bananas', 'Papayas', 'Cherries', 'Apples']
print(l1.index('Cherries')) #Result:2

#If we have multiple cherries, then that it will not give
l1 = ['Bananas', 'Papayas', 'Cherries', 'Apples','Cherries' ]
print(l1) #Result:['Bananas', 'Papayas', 'Cherries', 'Apples']
print(l1.index('Cherries')) #Result:2


#count– in List:
l1 = ['Bananas', 'Papayas', 'Cherries', 'Apples','Cherries','Cherries' ]
print(l1.count('Cherries')) #Result:3
print(l1.count('cherries')) #Result:0

#Reverse the items in the list/collection
l1 = ['Bananas', 'Papayas', 'Cherries','Pineapple','Apple','Orange','Melon']
print(l1[5:1:-1]) #Result:['Orange', 'Apple', 'Pineapple', 'Cherries']
print(l1[5:2:-2])  #Result:['Orange', 'Pineapple']

#Reverse– in List - Entire items will be in reverse order
#We should not give the reverse method in inside print, otherwise it will give “None”. 
#bcoz original object will not be changed if we give reverse method inside the print function

l1 = ['Bananas', 'Papayas', 'Cherries','Pineapple','Apple','Orange','Melon']
print(l1.reverse()) #Result:None
l1.reverse()
print(l1) #Result:['Bananas', 'Papayas', 'Cherries', 'Pineapple', 'Apple', 'Orange', 'Melon']

l1 = ['Bananas', 'Papayas', 'Cherries','Pineapple','Apple','Orange','Melon']
l1.reverse()
print(l1) #Result:['Melon', 'Orange', 'Apple', 'Pineapple', 'Cherries', 'Papayas', 'Bananas']




#sort - in list
# Don't print the sort, bcoz original object will not be changed if we give sort method inside the print function.
# We should not give the sort method in inside print function, otherwise it will give “None”.
l1 = ['Bananas', 'Papayas', 'Cherries','Pineapple','Apple','Orange','Melon']
print(l1.sort())#Result:None

l1 = ['Bananas', 'Papayas', 'Cherries','Pineapple','Apple','Orange','Melon']
l1.sort()
print(l1) #Result:['Apple', 'Bananas', 'Cherries', 'Orange', 'Papayas', 'Zfruit', 'apple']
#sort will arrange the items alphabetically i.e. in ascending order



#sort  - in list in descending/reverse order:
l1 = ['Bananas', 'Papayas', 'Cherries','Pineapple','Apple','Orange','Zfruit']
l1.sort()
print(l1) #Result:['Apple', 'Bananas', 'Cherries', 'Orange', 'Papayas', 'Zfruit']


l1.sort(reverse=True)
print(l1) #Result:['Zfruit', 'Papayas', 'Orange', 'Cherries', 'Bananas', 'Apple']




#sort  - in list Strings are case sensitive
l1 = ['Bananas', 'Papayas', 'Cherries','Apple','Orange','Zfruit','apple',"1"]
l1.sort()
print(l1) #Result:['Apple', 'Bananas', 'Cherries', 'Orange', 'Papayas', 'Zfruit', 'apple']

l1.sort(reverse=True)
print(l1) #Result:['apple', 'Zfruit', 'Papayas', 'Orange', 'Cherries', 'Bananas', 'Apple']


#ascii values - are American standard
# Basically string will convert into ascii values
# How to find the ascii value for the object?
#each character will be represented by hexa decimal value

print(ord('A'))
print(ord('1'))
print(ord('a'))


#sort in list - How to treat the strings equally (string lower, upper)
l1 = ['Bananas', 'Papayas', 'Cherries','Apple','Orange','Zfruit','apple',"1"]
print(l1) #Result:['Bananas', 'Papayas', 'Cherries', 'Apple', 'Orange', 'Zfruit', 'apple', '1']

l1.sort(key=str.lower)
print(l1) #Result:['1', 'Apple', 'apple', 'Bananas', 'Cherries', 'Orange', 'Papayas', 'Zfruit']

l1.sort(key=str.upper)
print(l1) #Result:['1', 'Apple', 'apple', 'Bananas', 'Cherries', 'Orange', 'Papayas', 'Zfruit']

l1.sort(reverse=True, key=str.lower)
print(l1) #Result: ['Zfruit', 'Papayas', 'Orange', 'Cherries', 'Bananas', 'Apple', 'apple', '1']

l1.sort(reverse=True, key=str.upper)
print(l1) #Result: ['Zfruit', 'Papayas', 'Orange', 'Cherries', 'Bananas', 'Apple', 'apple', '1']


#Alias method in list
l1 = ['Bananas', 'Papayas', 'Cherries']
print(l1) #Result:['Bananas', 'Papayas', 'Cherries']

l2 = l1
print(l2) #Result:['Bananas', 'Papayas', 'Cherries']

l1.append(10)

print(l1) #Result:['Bananas', 'Papayas', 'Cherries', 10]
print(l2) #Result:['Bananas', 'Papayas', 'Cherries', 10]


l2.clear()
print(l1) #Result:[]
print(l2) #Result:[]


#copy method in list
l1 = ['Bananas', 'Papayas', 'Cherries']
print(l1) #Result:['Bananas', 'Papayas', 'Cherries']

l2 = l1.copy()
print(l2) #Result:['Bananas', 'Papayas', 'Cherries']

l1.append(10)

print(l1) #Result:['Bananas', 'Papayas', 'Cherries', 10]
print(l2) #Result:['Bananas', 'Papayas', 'Cherries']


l2.clear()
print(l1) #Result:['Bananas', 'Papayas', 'Cherries', 10]
print(l2) #Result:[]


#sorted in list
l=[6,3,8]
s=sorted(l, key=None, reverse=True)
print(s) #Result:[8, 6, 3] 

#for loop and if condition
l=[1,1,1,1]
c=1
for i in l:
    if(i==1):
      c+=1
print(c) #Result: 5

#append method in list
l=[2,3.5,"chennai"]
l.append([2,3,4])
print(l) #Result:[2, 3.5, 'chennai', [2, 3, 4]]

#count in list
l=[1,2,3,4,2,1,3,5,9]
print(l.count(3)) #Result: 2

#for loop and if condition - find common numbers in the list
l=[1,2,3,4,5,6,7]
t=[2,6,9]
for i in l:
    if(i in t):
      print(i) #Result:26

#min & max method - find the minimum and maximum in the list
l1 = [10,20,30,50,23,56,34,56,78,-10]
print(max(l1)) #Result: 78
print(min(l1)) #Result: -10

#Membership Operator: - in & not in
l1 = [10,20,30,50,23,56,34,56,78,-10]
print(20 in l1) #Result:True
print('apple' in l1) #Result:False
print('apple' not in l1) #Result:True
print(56 not in l1) #Result:False


#Nested List - means one or more list
# list inside list
l1 = [[1,2,3],[4,5,6],[7,8,9]]
print(l1)  #Result:[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#Nested list - append list
l1 = [[1,2,3],[4,5,6],[7,8,9]]
l2 = [10,11,12]
l1.append(l2)
print(l1)  #Result:[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

#Nested list - Extend list
l1 = [[1,2,3],[4,5,6],[7,8,9]]
l2 = [10,11,12]
l1.extend(l2)
print(l1)  #Result:[[1, 2, 3], [4, 5, 6], [7, 8, 9], 10, 11, 12]
#extend will open up

#Nested list - index
l1 = [[1,2,3],[4,5,6],[7,8,9]]
print(l1[1]) #Result:[4, 5, 6]
print(l1[1][2]) #Result:6

#Nested list – index, range functions:
l = [["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"]]
print (l[1:4][2]) #Result:['j', 'k', 'l']






#List comprehension:
# comprehension Means short summary
# [items(expression) for item in collection]
# [items(expression) for item in collection, if condition == TRue]

names = ['Anna','john','carrie','alpha',"gord"]
names_with_a = []
for i in names:
    if 'a' in i:
       print(i)
#Result:Anna
# carrie
# alpha

names = ['Anna','john','carrie','alpha',"gord"]
names_with_a = []
for i in names:
    if 'a' in i:
        names_with_a.append(i)
print(names_with_a) #Result:['Anna', 'carrie', 'alpha']


#comprehension
# Below comprehension code is time efficient, space manage
# and in single line of code it will complete

# [items(expression) for item in collection]
names = ['Anna','john','carrie','alpha',"gord"]
names_with_a = [i for i in names]
print(names_with_a) #Result:['Anna', 'john', 'carrie', 'alpha', 'gord']

# [items(expression) for item in collection, if condition == TRue]
names = ['Anna','john','carrie','alpha',"gord"]
names_with_a = [i for i in names if  'a' in i]
print(names_with_a) #Result:['Anna', 'carrie', 'alpha']



double_from_0_to_10 = [number for number in range(11)]
print(double_from_0_to_10)#Result:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

double_from_0_to_10 = [number*2 for number in range(11)]
print(double_from_0_to_10)#Result:[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

double_from_0_to_10 = [number*1.5 for number in range(11)]
print(double_from_0_to_10)#Result:[0.0, 1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 10.5, 12.0, 13.5, 15.0]

double_from_0_to_10 = [number*1.5 for number in range(11) if (number*1.5)%2==0]
print(double_from_0_to_10)#Result:[0.0, 6.0, 12.0]"""

#####Nested List comprehension
matrix = []
for x in range(1,4):
    matrix.append(x)
print(matrix)#Result:[1, 2, 3]



matrix = []
for x in range(4):
    matrix.append(x)
print(matrix) #Result:[0, 1, 2, 3]



matrix = []
for x in range(4):
    matrix.append([])
    for y in range(4):
        matrix[x].append(y)
print(matrix)#Result:[[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]

#above code is written in below format
# below code is the Nested List comprehension
matrix = [[] for x in range(4)]
print(matrix) #Result:[[], [], [], []]

matrix1 = [[y for y in range(4)] for x in range(4)]
print(matrix1) #Result:[[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]

Mat1 = [[11, 12, 13],[14, 15, 16],[17, 18, 19]]
Mat2 = [[21, 22, 23],[24, 25, 26],[27, 28, 29]]
sum12 = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for i in range (len (Mat1)):
  for j in range (len (Mat2 [0])):
   sum12 [i][j] = Mat1 [i][j] + Mat2 [i][j]
  for k in sum12:
    print(k)
# Result:
# [32, 34, 36]
# [0, 0, 0]
# [0, 0, 0]
# [32, 34, 36]
# [38, 40, 42]
# [0, 0, 0]
# [32, 34, 36]
# [38, 40, 42]
# [44, 46, 48]



Mat1 = [[11, 12, 13],[14, 15, 16],[17, 18, 19]]
Mat2 = [[21, 22, 23],[24, 25, 26],[27, 28, 29]]
sum12 = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for i in range (len (Mat1)):
  for j in range (len (Mat2 [0])):
   sum12 [i][j] = Mat1 [i][j] + Mat2 [i][j]
for k in sum12:
  print(k)
#Result:
# [32, 34, 36]
# [38, 40, 42]
# [44, 46, 48]


#List Ord – comprehension:
a = [ord(i) for i in 'def']
print(a) #Result:[100, 101, 102]

a = 'def'
for i in a:
    print(ord(i))
#Result:100
# 101
# 102










