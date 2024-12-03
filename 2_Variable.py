x = 5
y = 10

print(x)
print(y)

print(type(x))
print(type(y))


#Casting:
a = str(3)
b = int(3)
c = float(3)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


#Variable name must start with a-z or A-Z or underscore
var = 10
var_iable = 10
var = 10

#Variable name must not start with numbers
"""1a = 2
print(1a)"""

#Variable name can use alphabets, underscore, alpha-numeric
abc_10 = 2
print(abc_10)

#Variable names are case sensitive:
age = 10
Age = 20
AGE = 30

#Assign Multiple Values to the Multiple Variables
x, y, z = "Apples", "Oranges", "tomato"
print(x, y, z) #Here we will be getting the separation by default

#if we want to customized separation, that also can be done:
x, y, z = "Apples", "Oranges", "tomato"
print(x, y, z, sep= ' ')
print(x, y, z, sep= '-----')

#printed in new line
x, y, z = "Apples", "Oranges", "tomato"
print(x, y, z, sep= '\n')

#One value to Multiple Variables:
a = b = c = 10
print(a, b, c, sep= '\n')

#Variable name which has meaning/purpose
time = 10
pay = 8
total_pay = time * pay
print(total_pay)

# Multiple Words in Variable Name
totalpay = 10
totalPay = 10  # camelCase
TotalPay = 10  # PascalCase
total_pay = 10 # snake_case

# Constants
PI = 3.14
GRAVITY = 9.8




