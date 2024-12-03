"""#Dictionaries: dict()
#{key:value}
#Items in the dictionaries will be stored as a key and value pair
#Items in dictionaries will be Ordered, Changeable, Allow duplicates value but not duplicate keys

#Dictionaries - Type and length
d1 = {
    'Name' : 'John',
    'Age' : 31,
    'Car': ['Ford','BMW'],
    'Married': True
}
print(d1) #Result:  {'Name': 'John', 'Age': 31, 'Car': ['Ford', 'BMW'], 'Married': True}
print(type(d1)) #Result: <class 'dict'>
print(len(d1)) #Result:4


#Items in the Dictionaries will be ordered after the python3.7 version
# Before 3.7 (i.e., 3.6 version below) - Dictionaries are unordered

#Items in the Dictionaries, we cannot access thuru indexes
# d1 = {
#     'Name' : 'John',
#     'Age' : 31,
#     'Car': ['Ford','BMW'],
#     'Married': True
# }
# print(d1[0]) #Result:KeyError


#Items in the Dictionaries, thuru keys we can access the values
d1 = {
    'Name' : 'John',
    'Age' : 31,
    'Car': ['Ford','BMW'],
    'Married': True
}
print(d1['Car']) #Result:['Ford', 'BMW']
print(d1['Name']) #Result:John


#Items in the Dictionaries, Allow duplicates value but not duplicate keys
#Different Key, Same Value
d1 = {
    'Name' : 'John',
    'Age' : 31,
    'Car': ['Ford','BMW'],
    'Married': True,
    'Married1': True
}
print(d1) #Result: {'Name': 'John', 'Age': 31, 'Car': ['Ford', 'BMW'], 'Married': True, 'Married1': True}

#Same Key, Different Value
d1 = {
    'Name' : 'John',
    'Age' : 31,
    'Car': ['Ford','BMW'],
    'Married': True,
    'Married': False
}
print(d1) #Result: {'Name': 'John', 'Age': 31, 'Car': ['Ford', 'BMW'], 'Married': False}


#get method in Dictionaries
d1 = {
    'Name' : 'John',
    'Age' : 31,
    'Car': ['Ford','BMW'],
    'Married': True
}
print(d1.get('Married')) #Result:True
print(d1.get('Car')) #Result:['Ford', 'BMW']

#Keys method in Dictionaries - It will print the list of keys names
d1 = {
    'Name' : 'John',
    'Age' : 31,
    'Car': ['Ford','BMW'],
    'Married': True
}
print(d1.keys()) #Result: dict_keys(['Name', 'Age', 'Car', 'Married'])

#Values method in Dictionaries - it will print the list values
d1 = {
    'Name' : 'John',
    'Age' : 31,
    'Car': ['Ford','BMW'],
    'Married': True
}
print(d1.values()) #Result:dict_values(['John', 31, ['Ford', 'BMW'], True])


#items method in Dictionaries - it will print the list of tuples
#Each item is tuple
#Each tuple will be key and value pair
# it will be separated by commas
d1 = {
    'Name' : 'John',
    'Age' : 31,
    'Car': ['Ford','BMW'],
    'Married': True
}
print(d1.items()) #Result:dict_items([('Name', 'John'), ('Age', 31), ('Car', ['Ford', 'BMW']), ('Married', True)])



#Clear method in Dictionaries
a={1:"A",2:"B",3:"C"}
a.clear()
print(a) #Result:{}


#List is converted into Dictionaries
# dict() => this is called as dict constructor
#List is given as => List of tuple values should be given in key, value pairs

l1 = [('a',1),('b',2),('c',3)]
d1 = dict(l1)
print(d1) #Result: {'a': 1, 'b': 2, 'c': 3}

#Zip Function in Dictionaries-by using list - Zip Functions will convert the key value pair into List of tuple of key value pairs
keys = ['a','b','c']
values = [1,2,3]
x = zip(keys,values)
print(x) #Result:<zip object at 0x0000027DF7C23EC0>  - Each time we refresh, the zip object code will be changed

x = list(zip(keys,values))
print(x) #Result:[('a', 1), ('b', 2), ('c', 3)]


#Zip Function in Dictionaries-by using list - If we give more keys, less values
keys = ['a','b','c','d','e']
values = [1,2,3]
x = zip(keys,values)
print(x) #Result:<zip object at 0x0000027DF7C23EC0>  - Each time we refresh, the zip object code will be changed

x = list(zip(keys,values))
print(x) #Result:[('a', 1), ('b', 2), ('c', 3)] - Here we have given 5 keys, 3 values. But it will consider only 3 keys


#Zip Function in Dictionaries - by using dict
keys = ['a','b','c','d','e']
values = [1,2,3]
x = zip(keys,values)
print(x) #Result:<zip object at 0x0000012E57CC3F80> - Each time we refresh, the zip object code will be changed

x = dict(zip(keys,values))
print(x) #Result:{'a': 1, 'b': 2, 'c': 3}


#When we convert the string into Dictionaries, we need ast module
# ast => means abstract syntax
# this ast module has literal_eval

import ast
st = "{'name': 'John', 'age':30}"
d1 = ast.literal_eval(st)
print(d1) #Result:{'name': 'John', 'age': 30}


#Items in the Dictionaries are changeable/replaceable
d1 = {
  'Name': 'John',
  'Age': 31,
  'Car': "Ford",
  "Year": 1991,
  'Married': True,
}
print(d1) #Result:{'Name': 'John', 'Age': 31, 'Car': 'Ford', 'Year': 1991, 'Married': True}
print(d1['Year']) #Result:1991

d1['Year'] = 2022
print(d1) #Result:{'Name': 'John', 'Age': 31, 'Car': 'Ford', 'Year': 2022, 'Married': True}

#Items in the Dictionaries are updatable
d1 = {
  'Name': 'John',
  'Age': 31,
  'Car': "Ford",
  "Year": 1991,
  'Married': True,
}
print(d1) #Result:{'Name': 'John', 'Age': 31, 'Car': 'Ford', 'Year': 1991, 'Married': True}
d1.update({'Year': 2030})
print(d1) #Result:{'Name': 'John', 'Age': 31, 'Car': 'Ford', 'Year': 2030, 'Married': True}


#Adding the items in Dictionaries:
d1 = {
  'Name': 'John',
  'Age': 31,
  'Car': "Ford",
  "Year": 1991,
  'Married': True,
}
print(d1) #Result:{'Name': 'John', 'Age': 31, 'Car': 'Ford', 'Year': 1991, 'Married': True}

#Adding
d1['Car Color'] = "red"
print(d1) #Result: {'Name': 'John', 'Age': 31, 'Car': 'Ford', 'Year': 1991, 'Married': True, 'Car Color': 'red'}

#update
d1.update({"Car Register": 2025, "Car Name": "BMW"})
print(d1)
#Result: {'Name': 'John', 'Age': 31, 'Car': 'Ford', 'Year': 1991, 'Married': True, 'Car Color': 'red', 'Car Register': 2025, 'Car Name': 'BMW'}


#pop method in Dictionaries - specific items will be removed:
d2 = {'Name': 'John', 'Age': 31, 'Car': 'Ford', 'Year': 1991, 'Married': True, 'Car Color': 'red', 'Car Register': 2025, 'Car Name': 'BMW'}
# d2.pop()
# print(d2) #TypeError: pop expected at least 1 argument, got 0

d2.pop('Married')
print(d2) #Result: {'Name': 'John', 'Age': 31, 'Car': 'Ford', 'Year': 1991, 'Car Color': 'red', 'Car Register': 2025, 'Car Name': 'BMW'}



#popitem method in Dictionaries - last item will be removed:
d2 = {'Name': 'John', 'Age': 31, 'Car': 'Ford', 'Year': 1991, 'Married': True, 'Car Color': 'red', 'Car Register': 2025, 'Car Name': 'BMW'}
d2.popitem()
print(d2) #Result:{'Name': 'John', 'Age': 31, 'Car': 'Ford', 'Year': 1991, 'Married': True, 'Car Color': 'red', 'Car Register': 2025}


#delete method in Dictionaries:
d1 = {'Name': 'John', 'Age': 31, 'Car': 'Ford', 'Year': 1991, 'Married': True, 'Car Color': 'red', 'Car Register': 2025, 'Car Name': 'BMW'}
del d1['Name']
print(d1)

#Empty Dictionaries - using for loop
count={}
count[(1,2,4)] =5
count[(4,2,1)] =7
count[(1,2)]= 6
count[(4,2,1)] =2
tot= 0
for i in count:
    tot= tot + count[i]
    print(len(count) + tot)

# Result:
# 8
# 10
# 16

count={}
count[(1,2,4)] =5
count[(4,2,1)] =7
count[(1,2)]= 6
count[(4,2,1)] =2
tot= 0
for i in count:
    tot= tot + count[i]
print(len(count) + tot)

# Result:
# 16

count={}
count[(1,2,4)] =5
count[(4,2,1)] =7
count[(1,2)]= 6
count[(4,2,1)] =2
tot= 0
for i in count:
    total= tot + count[i]
    print(len(count) + total)

# Result:
# 8
# 5
# 9

#For Loop in Dictionaries - Only printing Keys
d1 = {
  'Name': 'John',
  'Age': 31,
  'Car': "Ford",
  "Year": 1991,
  'Married': True,
  'Car Color': 'red',
  'Car Register': 2025,
  'Car Name': 'BMW'
}

for x in d1:
    print(x)
#Result:Name
# Age
# Car
# Year
# Married
# Car Color
# Car Register
# Car Name

#For Loop in Dictionaries - Only printing Values
d1 = {
  'Name': 'John',
  'Age': 31,
  'Car': "Ford",
  "Year": 1991,
  'Married': True,
  'Car Color': 'red',
  'Car Register': 2025,
  'Car Name': 'BMW'
}

for x in d1:
    print(d1[x])
#Result:
# John
# 31
# Ford
# 1991
# True
# red
# 2025
# BMW

#For Loop in Dictionaries - Only printing Keys - using key function
d1 = {
  'Name': 'John',
  'Age': 31,
  'Car': "Ford",
  "Year": 1991,
  'Married': True,
  'Car Color': 'red',
  'Car Register': 2025,
  'Car Name': 'BMW'
}

for x in d1.keys():
    print(x)
#Result:Name
# Age
# Car
# Year
# Married
# Car Color
# Car Register
# Car Name

#For Loop in Dictionaries - Only printing Values -  using value function
d1 = {
  'Name': 'John',
  'Age': 31,
  'Car': "Ford",
  "Year": 1991,
  'Married': True,
  'Car Color': 'red',
  'Car Register': 2025,
  'Car Name': 'BMW'
}

for x in d1.values():
    print(x)
#Result:John
# 31
# Ford
# 1991
# True
# red
# 2025
# BMW

#For Loop in Dictionaries - I want to print both keys and values - items function:
#It will return key, value pairs in tuple format
d1 = {
  'Name': 'John',
  'Age': 31,
  'Car': "Ford",
  "Year": 1991,
  'Married': True,
  'Car Color': 'red',
  'Car Register': 2025,
  'Car Name': 'BMW'
}

for x in d1.items():
    print(x)
#Result:('Name', 'John')
# ('Age', 31)
# ('Car', 'Ford')
# ('Year', 1991)
# ('Married', True)
# ('Car Color', 'red')
# ('Car Register', 2025)
# ('Car Name', 'BMW')

#For Loop in Dictionaries - I want to print both keys and values - items function:
d1 = {
  'Name': 'John',
  'Age': 31,
  'Car': "Ford",
  "Year": 1991,
  'Married': True,
  'Car Color': 'red',
  'Car Register': 2025,
  'Car Name': 'BMW'
}

for x,y in d1.items():
    print(x,y) #It will return key, value pairs in normal format
#Result:
# Name John
# Age 31
# Car Ford
# Year 1991
# Married True
# Car Color red
# Car Register 2025
# Car Name BMW

#For Loop in Dictionaries - I want to print both keys and values - items function - printing using f string:
d1 = {
  'Name': 'John',
  'Age': 31,
  'Car': "Ford",
  "Year": 1991,
  'Married': True,
  'Car Color': 'red',
  'Car Register': 2025,
  'Car Name': 'BMW'
}

for x,y in d1.items():
    print(f'{x = } and {y= }') #It will return key, value pairs
#Result: x = 'Name' and y= 'John'
 # x = 'Age' and y= 31
 # x = 'Car' and y= 'Ford'
 # x = 'Year' and y= 1991
 # x = 'Married' and y= True
 # x = 'Car Color' and y= 'red'
 # x = 'Car Register' and y= 2025
 # x = 'Car Name' and y= 'BMW'

#Another Way
d1 = {
  'Name': 'John',
  'Age': 31,
  'Car': "Ford",
  "Year": 1991,
  'Married': True,
  'Car Color': 'red',
  'Car Register': 2025,
  'Car Name': 'BMW'
}

for key,value in d1.items():
    print(f'{key} and {value}') #It will return key, value pairs

# Result:Name and John
# Age and 31
# Car and Ford
# Year and 1991
# Married and True
# Car Color and red
# Car Register and 2025
# Car Name and BMW

#Another Way
d1 = {
  'Name': 'John',
  'Age': 31,
  'Car': "Ford",
  "Year": 1991,
  'Married': True,
  'Car Color': 'red',
  'Car Register': 2025,
  'Car Name': 'BMW'
}

for key,value in d1.items():
    print(f'{key = } and {value = }') #It will return key, value pairs

# Result:key = 'Name' and value = 'John'
# key = 'Age' and value = 31
# key = 'Car' and value = 'Ford'
# key = 'Year' and value = 1991
# key = 'Married' and value = True
# key = 'Car Color' and value = 'red'
# key = 'Car Register' and value = 2025
# key = 'Car Name' and value = 'BMW'


#How to sort the elements in Dictionaries - using sorted function:
#Sorted (collection, key = function)
#Note: Original Dictionaries will not be sorted - only new Dictionaries can be sorted
# Original Dictionaries will remain same. Only new  Dictionaries can be modified
d1 = {
    'a': 3,
    'c': 4,
    'b': 1,
    'd': 2
}
print(d1.items()) #Result:dict_items([('a', 3), ('c', 4), ('b', 1), ('d', 2)])  - Here key in '0th' index and value is '1st' index
#Here we need to decide, by using keys we are going to sort or by using values we are going to sort.That part we only need to decide

#Using keys, we are sorting
d1 = {
    'a': 3,
    'c': 4,
    'b': 1,
    'd': 2
}
x  = sorted(d1.items()) #if we want to print in {} curly bracket format, then we need to use dict function. Else it will print in list of tuple format
print(x) #Result:[('a', 3), ('b', 1), ('c', 4), ('d', 2)]

x  = dict(sorted(d1.items())) #dict has been used to print in {} curly bracket format
print(x) #Result:{'a': 3, 'b': 1, 'c': 4, 'd': 2}

#Using values, we are sorting - using lambda function
# Sorted (collection, key = function)
d1 = {
    'a': 3,
    'c': 4,
    'b': 1,
    'd': 2
}
x  = dict(sorted(d1.items(), key = lambda item:item[1]))
print(x) #Result:{'b': 1, 'd': 2, 'a': 3, 'c': 4}

#Using keys, we are sorting - using lambda function
# Sorted (collection, key = function)
d1 = {
    'a': 3,
    'c': 4,
    'b': 1,
    'd': 2
}
x  = dict(sorted(d1.items(), key = lambda item:item[0]))
print(x) #Result:{'a': 3, 'b': 1, 'c': 4, 'd': 2}

#How to pass the Dictionaries in function
d1 = {
    'a': 3,
    'c': 4,
    'b': 1,
    'd': 2
}

def function(d):
   for x,y in d.items():
       print(x,y)

function(d1) #Result:a 3
# c 4
# b 1
# d 2

#How to pass the Dictionaries in function - sorted function
d1 = {
    'a': 3,
    'c': 4,
    'b': 1,
    'd': 2
}

def function(d):
   for x,y in sorted(d.items()):
       print(x,y)

function(d1)#Result:a 3
# b 1
# c 4
# d 2

#How to pass the Dictionaries in function - sorted function - sorting values
d1 = {
    'a': 3,
    'c': 4,
    'b': 1,
    'd': 2
}

def function(d):
   for x,y in sorted(d.items(), key= lambda a: a [1]):
       print(x,y)

function(d1) #Result:b 1
# d 2
# a 3
# c 4"""

#How to pass the Dictionaries in function - sorted function - sorting keys
d1 = {
    'a': 3,
    'c': 4,
    'b': 1,
    'd': 2
}

def function(d):
   for x,y in sorted(d.items(), key= lambda a: a [0]):
       print(x,y)

function(d1) #Result:a 3
# b 1
# c 4
# d 2
