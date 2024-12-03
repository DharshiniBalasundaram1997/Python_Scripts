
#Single Line Comment

#Multi Line Comment
"""print("Hello World 2")"""

#help()
#help(print)
#__doc__
def add(a,b):
    """ This function takes two numbers as input and returns their sum"""
    return a + b
#print(add.__doc__)

#Int Data Type:
print(10)

#Float Data Type:
print(10.20)
print(10.)
print(2e10)

#Complex
print(10 + 2j)


#type
print(type(10))
print(type(10.2))
print(type(10 + 2j))


#Strings:  we can use double quotes of single quotes
print("Hello World")
print('Hello World')
print(type("Hello World"))

#Booleans: True and False
print(True)
print(False)
print(type(True))
print(type(False))


# None: Absence of a value
print(None)
print(type(None))


#Sequences:
#1. Strings
s1 = 'Hello World'
print(s1)

#2. Lists : Square Brackets
l1 = [10, 20, 30, 40]
print(l1)
print(type(l1))

#3. Tuples : Round Brackets
t1 = (10, 20, 30, 40)
print(t1)
print(type(t1))

#Sets
s1 = {10, 20, 30, 40}
print(s1)
print(type(s1))

#Dictoniaries
d1 = {
'Name': 'John',
'Age': 31
}
print(d1)
print(type (d1))