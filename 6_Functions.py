#Functions - All Functions we need to call, then only it will run

# Function is => A block of code which only runs when it is called
print("hello")


print(type("hello"))

#Methods will work on 1 particular class

##################Defining a function
def greeting():
    print("Hello World!!!!!")

#Calling a Function
greeting()





################type of function
print(type(greeting()))

#type of object
print(type('abc'))

x = type ('ccc')
print(x)

x = len('mba')
print(x)

print(len('Hello'))





###########Printing the function: it will return none
def greeting():
    print("Hellllloooooooooo")

print(greeting())


############Returning the values from the Function - By using Return Keyword:
def greeting():
    return 'Worldddd'

print(greeting())








#############How to return the multiple values - By using Return Keyword
def greeting():
    a = 1
    b = 2
    return a,b

print(greeting())

#or

def greeting():
    a = 1
    b = 2
    return a,b

n1, n2 = greeting()
print(n1)
print(n2)

#or - tuples

def greeting():
    a = 1
    b = 2
    return (a,b)

result = greeting()
print(result) #Result = (1,2)

#or - tuple - brackets
def greeting():
    a = 1
    b = 2
    return [a,b]

result = greeting() #Functions are first class objects => For variable we are assigning the functions, that is called as first class objects
print(result) #Result = [1,2]


############## One function can be called in another function
def multiply (x, y):
    return x * y

def apply(funct, x, y):
    return funct(x, y)

result = apply(multiply,5, 2)
print(result) #Result = 10


################### Formal Arguments(Parameters) and Actual Arguments(Arguments)

# Variables are inbuilt Function signature - Formal Arguments
# Values are actual arguments

def f1(x, y):
    return x * y

print(f1(5, 2)) #Result = 10


######Pass By Object Reference - When we are passing the object to the function , it will receive the reference to the objects
def my_function(my_list):
    my_list.append(1)

l1 = [2,3,4]
print(l1)

my_function(l1) #mutable object
print(l1)




def my_function(text):
    text += 'World'

t1 = 'Hello'
print(t1)

my_function(t1) #mutable object
print(t1)


############ Positional Argument - we can pass the positional arguments to the functions and we can pass as many as parameters but it should be in specific order
def my_function (x, y):
    return x * y

res = my_function(5,10)
print(res)


######## If we don't know how many parameters/ arguments we are going to pass then we can use Arbitrary Arguments
######## Arbitrary Arguments => * is args (astricks)
def my_function(*name):
   print('Hello ' ,name)

my_function('Mr. A', 'Mr. B', 'Mr. C', 'Mr. D', 'Mr. E')
my_function('Mr. A', 'Mr. B', 'Mr. C', 'Mr. D', 'Mr. E', 'Mr. F')


# For loop - Arbitrary Arguments
def my_function(*name):
    for each_name in name:
        print('Hello ' ,each_name)

my_function('Mr. A', 'Mr. B', 'Mr. C', 'Mr. D', 'Mr. E')
my_function('Mr. A', 'Mr. B', 'Mr. C', 'Mr. D', 'Mr. E', 'Mr. F')





############ Arbitrary KeyWord Arguments => We no need to follow the order
def my_function (x, y):
    print(x)
    print(y)

#key = value
my_function(5,10)

#Note: We can change the values of x and Y
def my_function (x, y):
    print(x)
    print(y)

#key = value
my_function(y=5,x=10)


####Arbitrary KeyWord Arguments => double astricks **kwargs
def my_function (**details):
    print(details)

my_function (name='A', surname='B', age=27, height=175)


##### For loop - Arbitrary KeyWord Arguments => double astricks **kwargs
def my_function (**details):
    for values in details:
        print(values)

my_function (name='A', surname='B', age=27, height=175)


def my_function (**details):
    for key, values in details.items():
        print(key, values)

my_function (name='A', surname='B', age=27, height=175)


#Tuple #List
def my_function(number):
    print(number)

my_function({10,20,30,40,50}) #Tuple
my_function([10,20,30,40,50]) #List


###########Default Parameter Value:
def my_function(name = 'user') :
   print(name)

my_function('Python')
my_function('Java')
my_function ()








############# Scope (There is particular Range)
# Two Types - Global Scope Variable(inside & outside of the function), Local Scope Variable (inside the function)

#Global Variable
x = 10 #Global Variable
print(x)

def f1():
    print(x)

f1()


####Local Variable
x = 10 #Global Variable
print(x)

def f1():
    y = 5
    print(y)
    print(x)

f1()
# print(y)



######What happens if we give the same name as global and local variable:
x = 10  #Global Variable
print(x)

def f1():
    x = 5 #Local Variable
    print(x)

f1()
print(x)



######Global Keyword
x = 10  #Global Variable
print(x)

def f1():
    global x
    x = 5 #global
    print(x)

f1()
print(x)



############# Recursion - is a statement, we can call the function repeatedly

#Factorial = 5! = 5 x 4 3 x 2 x 1

def factorial(n):
 if n == 1:
     return 1
 else:
     return n * factorial(n-1)

print(factorial(5))




############ Maximum recursion Depth:
def factorial(n):
    factorial(n)

print(factorial(4))