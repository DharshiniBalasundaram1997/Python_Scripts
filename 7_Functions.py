#######Lambda Function - Small and anonymous function

# anonymous -> Meaning No Name

#It can take any number of arguments & it will work on 1 expression only

#Lambda     Arguments: expression
       #Any argumnets: 1 expression (Expression is nothing buy variable


def f1(x):
   return x + 10

print(f1(5))


#instead of above function, we can use lambda function

a = lambda x: x+ 10
print(a(5))


#We can pass many arguments, but 1 expression
a = lambda x, y, z: x + y + z
print(a(5, 10, 15))


#Creating square function using lambda expression
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def four(x):
    return x ** 4
#By changing its values continuously , it's a tedious task. so we are using lamba

# Instead of creating 3 functions, we can create 1 function by using lambda expression
def power(n):
    return lambda a: a ** n

square = power(2)
cube = power(3)
fourth_power = power(4)

print(square(2))
print(cube(2))
print(fourth_power(2))


##########Reverse String:
str1 = 'hello'

txt = lambda string: string.upper()[::-1]

print(txt(str1))



###############Decorators:
#Decorators will acts as a wrapper. It will wrap the 1 function by another function.
def mk(x):
  def mk1():
   print("Decorated")
   x()
  return mk1


def mk2():
  print("Ordinary")

p = mk(mk2)
p()


def my_decorator(func):
    def wrapper():
        print("Something is happening, BEFORE the function is called")
        func()
        print("Something is happening, AFTER the function is called")
    return wrapper

def say_hello():
    print('Hello')


deco = my_decorator(say_hello)
deco()


#simplified way
def my_decorator(func):
    def wrapper():
        print("Something is happening, BEFORE the function is called")
        func()
        print("Something is happening, AFTER the function is called")
    return wrapper()

@my_decorator
def say_hello():
    print('Hello')

# say_hello()


###############Generators: It is a function, it will pause the function (yield keyword)
#  pause = yield keyword

def genrator():
    yield 1
    yield 2
    yield 3

for x in genrator():
  print(x)
  print(x ,'is a number')
  print(x, 'runs from a generator')
  print(x, 'will now move to the next YIELD number')
  print('============================================')


def genrator():
    yield 1
    yield 2
    yield 3

x = genrator()

print(next(x))
print(next(x))
print(next(x))




#fibonicci series
# 0 1 1 2 3 5 8 13

def fibo(limit):
    a, b = 0, 1

    while a < limit:
        yield a
        a,b = b,a + b

x = fibo(5)
print(next(x))
print(next(x))
print(next(x))

#print fibonicc series from 0 to 100
def fibo(limit):
    a, b = 0, 1

    while a < limit:
        yield a
        a,b = b,a + b

for x in fibo(100):
    print(x)