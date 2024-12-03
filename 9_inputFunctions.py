#input() function: It will takes input() as a -> String

user = input()
print(user)
print(type(user))

#Even If we pass input as number, by default it will take as a string

user = input("Enter Someting:")
print(user)
print(type(user))


#int() function, -> Here String is converted into int . So this is called casting
user = int(input("Enter Someting:"))
print(user)
print(type(user))

# float() function, -> Here String is converted into float . So this is called casting
user = float(input("Enter Someting:"))
print(user)
print(type(user))


# complex() function -> Here String is converted into complex . So this is called casting
user = complex(input("Enter Someting:"))
print(user)
print(type(user))


# List(),tuple(), set(), dict()
user = list(input("Enter Someting:"))
print(user)
print(type(user))

user = tuple(input("Enter Someting:"))
print(user)
print(type(user))

user = set(input("Enter Someting:"))
print(user)
print(type(user))



# map() -> Runs a function on all items on a collection

collection = [10, 20, 30, 40, 50]
collection2 = [] #by using list

for x in collection:
    collection2.append(float(x))

print(collection2)

# we can use above code in map format
collection = [10, 20, 30, 40, 50]
collection2 = list(map(float,collection))
print(collection2)

double = list(map(lambda x: x * 2 , collection))
print(double)


# Filter() - Runs a function on all items on a collection
# but only stores a true value

age = [14, 18, 21, 25, 26, 19, 20, 14, 13, 10, 8, 7, 34, 45]

def adult(x):
    if x >=18:
        return True
    else:
        return False

adults = list(filter(adult, age))
print(adults)


# we can use below code as well
age = [14, 18, 21, 25, 26, 19, 20, 14, 13, 10, 8, 7, 34, 45]
def adult(x):
    return x >= 18

adults = list(filter(adult, age))
print(adults)


# we can use below code as well
age = [14, 18, 21, 25, 26, 19, 20, 14, 13, 10, 8, 7, 34, 45]
adults = list(filter(lambda x:x>=18, age))
print(adults)