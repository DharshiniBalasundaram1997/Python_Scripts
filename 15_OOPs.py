"""# OOPS -  Object Oriented Programming System:
# Objects -> has data -> data has code

#Encapsulation - It will hide the Object details
#Inheritance - The methods of one class will be given to another class - like hierarchy (Parent - child)
# Polymorphism - One method will respond in different different ways
# Abstraction - it will define, how to work with object


# OOPS Concept is ->  implementation of classes and objects




# OOPS Concept – Object:
# Object is nothing but a character, number i.e=> Different data types are objects
x = 'Hello'  #Here Hello is an Object
print(type(x)) #Result: <class 'str'> - x belongs to class string

x = 10   #Here 10 is an Object
print(type(x)) #Result:<class 'int'> - x belongs to class integer

x = 10.0   #Here 10.0 is an Object
print(type(x)) #Result:<class 'int'> - x belongs to class float

x = 10.0j   #Here 10.0j is an Object
print(type(x)) #Result:<class 'complex'> - x belongs to class complex


#Each Object in Python, It will dependent to certain classes.
#We can create our own classes and Objects.



#OOPS - Create a Class:

#Creating Code for the bank. We need to create a list and Which includes 10,000 customers. So we need to create 10,000 customers
# But how are we going to maintain the records? - by using class es and objects

#Maintanability of the code should be best - if we use classes and objects



class Customer: #class -> is a keyword and Customer is Class Name
    pass


#Create a Object:
c1 = Customer()  #c1 -> is the object
print(c1) #Result:<__main__.Customer object at 0x000002B45B4355B0>
print(type(c1)) #Result:<class '__main__.Customer'>


# Attributes (Attributes is nothing but Variables. In Class the Attributes will be present.)

# 3 Types of Attributes:
# 1. Instance Attributes - Attributes will belong to objects
# 2. Class Attributes - Each Object will be belonged
# 3. Local Attributes -







# Class Attributes/Variables - Each Object will share the variables which are present in class :

#Create a Class
class Customer:

    #Class Attributes (Variables)
    bank_name = 'ABCD Bank'  #Static or class level variables

#Create a Object
c1 = Customer()
print(c1.bank_name) #Result: ABCD Bank


c2 = Customer()
print(c2.bank_name) #Result: ABCD Bank





#How to Create a Methods in class: - self
# Defining a function inside a class -> is called Method

#Create a Class
class Customer:

    #Class Attributes (Variables)
    bank_name = 'ABCD Bank'  #Static or class level variables

    #Create a Method (Methods means Function/ Function means Method)
    def greet(self):
      print('Hi Welcome to ABCD BANK')

#Create a Object
c1 = Customer()
c1.greet()   #Result: Hi Welcome to ABCD Bank

c2 = Customer()
c2.greet()   #Result: Hi Welcome to ABCD Bank

c3 = Customer()
print(c3.bank_name)   #Result: ABCD Bank





# What is self ?
# #Self -> means Parameter

#Create a Class
class Customer:

    #Class Attributes/Variables
    bank_name = 'ABCD Bank'

    #Create a Method/Function
    def greet(aa):  #instead of self we can give any name
      print(f'Hi Welcome to {aa.bank_name}')

#Create a Object
c1 = Customer()
c1.greet() #Result: Hi Welcome to ABCD Bank
Customer.greet(c1) #Result: Hi Welcome to ABCD Bank   -c1 acts as self

"""


#Updating the Values:
class Customer:

    bank_name = 'ABCD Bank'

    def greet(aa):
      print(f'Hi Welcome to {aa.bank_name}')

#Create a Object
c1 = Customer()
print(c1.bank_name) #Result:ABCD Bank

c2 = Customer()
print(c2.bank_name) #Result:ABCD Bank

c1.bank_name = 'XYZ Bank'
print(c1.bank_name) #Result:XYZ Bank
print(c2.bank_name) #Result:ABCD Bank

#Each Object can have different different values
#Object is c1, c2
