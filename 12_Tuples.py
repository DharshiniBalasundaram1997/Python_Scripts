
"""#Tuples: Represented in round brackets
# All elements will be separated by coma
# Items in tuple are Ordered , Immutable, Allow Duplicates

t1 = (10,20,30,40,50)
print(t1) #Result: (10, 20, 30, 40, 50)
print(type(t1)) #Result: <class 'tuple'>
print(len(t1)) #Result: 5

# Tuple – int - not considered as tuple::
# t1 = (10)
# print(t1) #Result: 10
# print(type(t1)) #Result: <class 'int'>
# print(len(t1)) #Result: Error

# Output of the tuple will always be in bracket.
# Tuples should always be separated by comma. 
# But here only one value we have given. So it is not considered as tuple


# Tuple – string - not considered as tuple:
t1 = ('Apple')
print(t1) #Result: Apple
print(type(t1)) #Result: <class 'str'>
print(len(t1)) #Result: 5
# Output of the tuple will always be in bracket.
# Tuples should always be separated by comma . But here only one value we have given.
# So it is not considered as tuple


#Tuple - for 1 string or number - separated by comma
t1 = ('Apple',)
print(t1) #Result: ('Apple',)
print(type(t1)) #Result: <class 'tuple'>
print(len(t1)) #Result: 1

t1 = (1,)
print(t1) #Result: ('1',)
print(type(t1)) #Result: <class 'tuple'>
print(len(t1)) #Result: 1

#Where the Tuple is Ordered, Immutable and Allow Duplicates:
t1 = ('A','b','c','d') #Tuple can be  string
print(t1)#Result:('A', 'b', 'c', 'd')
print(type(t1))#Result:<class 'tuple'>

t1 = (10,20,30,40,10.78, 5+9j) #Tuple can be integers/float/complex,
print(t1)#Result:(10, 20, 30, 40, 10.78, (5+9j))
print(type(t1))#Result:<class 'tuple'>

t1 = (True,False,False,True,True) #Tuple can be collection of boolean
print(t1)#Result:(True, False, False, True, True)
print(type(t1))#Result:<class 'tuple'>

t1 = (10,20,'a','b',True,False) #Tuple can be mixed data type
print(t1)#Result:(10, 20, 'a', 'b', True, False)
print(type(t1))#Result:<class 'tuple'>


#Tuples will be ordered:
t1 = (10,20,30,40,50)
print(t1) #Result:(10, 20, 30, 40, 50)

#Tuple by index
print(t1[2]) #Result:30

#Tuple by range function
print(t1[2:5])#Result:(30, 40, 50)
print(t1[:5])#Result:(10, 20, 30, 40, 50)
print(t1[0:])#Result:(10, 20, 30, 40, 50)
print(t1[::2])#Result:(10, 30, 50)

#reverse the tuple
t1 = (10,20,30,40,50)
print(t1[::-1]) #Result:(50, 40, 30, 20, 10)

print(t1[-1:-5:-1]) #Result:(50, 40, 30, 20)



# Tuples cannot be changeable or tuples cannot be modifiable
#But if we want to modify the tuple, then we can convert the tuple in list and we can perform the modifications and then convert into tuple
t1 = (10,20,30,40,50)
print(t1) #Result:(10, 20, 30, 40, 50)

#HEre we are converting the tuple into list
l1 = list(t1)
print(l1) #Result:[10, 20, 30, 40, 50]

#Tuple - append
l1.append('Orange')
print(l1) #Result:[10, 20, 30, 40, 50, 'Orange']

#Tuple - pop
l1.pop(2)
print(l1) #Result:[10, 20, 40, 50, 'Orange']

#Tuple - index modify
l1[0] = 'Mango'
print(l1) #Result:['Mango', 20, 40, 50, 'Orange']

#Here we converted the list into tuple
t2 = tuple(l1)
print(t2) #Result:('Mango', 20, 40, 50, 'Orange')

#Tuple - Min,Max, Count
a=(1,2,3,2,3,4,5)
print(min(a)+max(a)+a.count(2)) #Result: 1+5+2 = 8

#Print in Tuple
T=tuple("tuple")
print(T) #Result:('t', 'u', 'p', 'l', 'e')

a=(1,2,3,2,3,4,5)
print(tuple(a)) #Result:(1, 2, 3, 2, 3, 4, 5)


# Tuples - Packing and UnPacking:
# Tuples - Packing:
t1 = ('A','B','C') #This is packing
print(t1) #Result:('A', 'B', 'C')


# Tuples - UnPacking:
# Unpacking means  -> extracting the each value and giving into separate variable
t2 = ('A','B','C') #This is packing
print(t2) #Result:('A', 'B', 'C')

a,b,c = t2 #a,b,c - each variable will be assigned to the t2 value

print(a)#Result: A
print(b)#Result: B
print(c)#Result: C


#Tuples - UnPacking - ValueError: too many values to unpack
# t2 = ('A','B','C','D','E')
# print(t2) #Result:('A', 'B', 'C', 'D', 'E')
#
# a,b,c = t2
#
# print(a)
# print(b)
# print(c)

#Tuples - UnPacking - In Order to overcome the ValueError: too many values to unpack- Use asterisks
t2 = ('A','B','C','D','E')
print(t2) #Result:('A', 'B', 'C', 'D', 'E')

a,b,*c = t2

print(a) #Result:A
print(b) #Result:B
print(c) #Result:['C', 'D', 'E']

#Tuples - UnPacking -In Order to overcome the ValueError: too many values to unpack- Use asterisks
# Changing the position of asterisks
t2 = ('A','B','C','D','E')
*a,b,c = t2

print(a) #Result:['A', 'B', 'C']
print(b) #Result:D
print(c) #Result:E


a,*b,c = t2

print(a) #Result:A
print(b) #Result:['B', 'C', 'D']
print(c) #Result:E


#Joining the Tuples
t1  = ('A','B','C')
t2 = ('D','E','F')

t3 = t1 + t2
print(t3) #Result:('A', 'B', 'C', 'D', 'E', 'F')

t3 = t1 * 3
print(t3) #Result:('A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C')


#tuples - directory
t1 = ('A', 'B', 'C')
t2 = ('D', 'E' , 'F')

print(dir(t1)) #2 methods we have - count and index


#Tuples - count
t1 = ('A', 'B', 'C','B','B','B','B','B','B','B')
print(t1.count('B'))#Result:8

#Tuples - index
t1 = ('A', 'B', 'C','B','B','B','B','B','B','B')
print(t1.index('B'))#Result:1


#Joining the Tuples - string
tup_1 = (5,4)
tup_2 = (1,6)
a = tup_1 + tup_2
print(str(a)) #Result:(5, 4, 1, 6)

#Tuples inside tuple- index
a= (1,2,3,(4,5,6))
print(a[3][0]) #Result:4

#Tuple Append - Tuple cannot be modified
# tuple=(1,3,5,7,9)
# a= tuple.append(11)
# print(a)"""


