#####Strings - Collection of character
from typing import Concatenate

print("Hello World") #Result:Hello World
print ('Hello World') #Result:Hello World

print(type("Hello World !!")) #Result:<class 'str'>
print(type('Hello World !!')) #Result:<class 'str'>

#####Single Line string -> either we can give single quotes or double quotes
a = 'Hello'
b = 'World'

print(a,b, sep='\n')
#Result:
# Hello
# World
print(type(a),type(b), sep='\n')
#Result:
# <class 'str'>
# <class 'str'>



#####MultiLine String -> either we can give single quotes or double quotes

a = ('''Hello 
     This 
will 
now 
be 
a 
multi Line String''')
print(a)

#Result:
# Hello
#      This
# will
# now
# be
# a
# multi Line String

#####Length of String
b = "Hello World"
print(len(b)) #Result:11


#####Directory
print(dir(b))


#####Split
b = "Hello World"
print(b.split()) #Result:['Hello', 'World']

#####Split , len- Find How many words are there?
b = "Hello World"
print(len(b.split())) #Result:2

s="hello world"
l=s.split()
print(l) #Result:['hello', 'world']
print(l[0]) #Result: hello
print(l[1]) #Result: world

#####How to repeat the strings -  * (astericks is used for multiplication purpose)
c = "Hello World "
print(c) #Result:Hello World
print(c * 3) #Result:Hello World Hello World Hello World


# another way
c = "Hello World "
d = c * 3
print(d) #Result:Hello World Hello World Hello World


#####Strings are immutable (immutable means we cannot modify)



#####How to check the particular object in the string?
a = "Hello! This is Python. I am a Programming Language"
print(a)  #Result:Hello! This is Python. I am a Programming Language

print('is' in a) #Result:True
print('Programming' in a) #Result:True
print('Java' not in a) #Result:True
print('C++' in a) #Result:False

#How to check the particular letter, in the string?
####Index – Positive index:
a = "Hello World"
print(a) #Result:Hello World
print(a[4]) #Output = o

####Index – Negative Index:
a = "Hello World"
print(a) #Result:Hello World
print(a[-7]) #Output = o

####Index – Out of Range:
a = "Hello World"
print(a) #Result:Hello World
# print(a[45]) #Result: Error

#Slicing
# variable [Start:End-1]
a = "Hello World"
print(a) #Result:Hello World
print(a[2:5]) #Result:llo
print(a[0:5]) #Result:Hello

# Even if we didn’t give 0, it will take from start(0)
print(a[:5]) #Result:Hello

#Even if we didn’t give end position, it will take end word
print(a[6:]) #Result:World

print(a[:]) #Result:Hello World

# variable [Start:End-1:Step]
a = "Hello World"
print(a) #Result: Hello World

print(a[::3]) #Result: HlWl
print(a[::-3]) #Result: dooe

print(a[2:9:3]) #Result:l r


#Reverse the string - By using slicing   ::-1-> meaning of this symbol is reverse slicing
a = "Hello World"
reverse_a = a[ ::- 1]

print(reverse_a) #Result: dlroW olleH



######String - Methods

a = 'Hello World'
print(dir(a)) #Result: ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']



########Case Modification:

#capitalize - Only first letter will turn to capital word
a = 'Hello WORLD'
print(a) #Result:Hello WORLD
print(a.capitalize()) #Result:Hello world


#capitalize - Only first letter will turn to capital word
a = 'Hello WORLD'
b = (a.capitalize())
print(b +'\n') #Result:Hello world

#Casefold - is like case sensitive (Example: like german characters it will take and convert)
#Casefold will turn all letters to LowerCase
a = 'Hello WORLD'
b = (a.casefold())
print(b) #Result:hello world

#lower - Lower will turn all letters to LowerCase
a = 'Hello WORLD'
b = (a.lower())
print(b) #Result:hello world

#swapcase - LowerCase will turn to uppercase & UpperCase will turn to LowerCase
a = 'Hello WORLD'
b = (a.swapcase())
print(b) #Result:hELLO world

#Upper  - Upper will turn all letters to UpperCase
a = 'Hello WORLD'
b = (a.upper())
print(b) #Result:HELLO WORLD


#title  - Every first word will turn to capital
a = 'hello world'
b = (a.title())
print(b) #Result:Hello World





#######String Methods - is

# alnum - is alpha numeric
a = 'hello07 1  world'
b = (a.isalnum())
print(b) #Result:False

a = 'hello0world'
b = (a.isalnum())
print(b) #Result:True

#isalpha - Only Letters
a = 'helloworld'
b = (a.isalpha())
print(b) #Result:True

a = 'hello1world'
b = (a.isalpha())
print(b) #Result:False

#isdigit
a = '1234'
b = (a.isdigit())
print(b) #Result:True

a = 'Hello 1234'
b = (a.isdigit())
print(b) #Result:False

#islower
a = 'abc'
b = (a.islower())
print(b) #Result:True

a = 'ABCxx'
b = (a.islower())
print(b) #Result:False

#isUPPER
a = 'ABC'
b = (a.isupper())
print(b) #Result:True

a = 'ABCxx'
b = (a.isupper())
print(b) #Result: False


#istitle
a = 'Hello World'
b = (a.istitle())
print(b) #Result: True

a = 'Hello world'
b = (a.istitle())
print(b) #Result: False

#isnumeric
a = '1234'
b = (a.isnumeric())
print(b) #Result: True

a = 'HelloWorld1234'
b = (a.isnumeric())
print(b) #Result: False

#replace
a = 'Hello world'
b = (a.replace('o', '********'))
print(b) #Result: Hell******** w********rld

#Strip - will remove the spaces of starting and ending
a = '   Hello world        '
b = (a.strip())
print(b) #Result: Hello world

#lStrip - it will remove spaces of left side only
a = '   Hello world        '
b = (a.lstrip())
print(b) #Result: Hello world

#rStrip - it will remove spaces of right side only
a = '   Hello world        '
b = (a.rstrip())
print(b) #Result:   Hello world

#Stripping the symbols of starting and ending
a = '---------Hello world-----------'
b = (a.rstrip('-'))
c = (a.lstrip('-'))
d = (a.strip('-'))
print(b) #Result: ---------Hello world
print(c) #Result: Hello world-----------
print(d) #Result: Hello world

#Startswith
a = '---------Hello world-----------'
print(a.startswith('---------')) #Result:True
print(a.startswith('---------Hello world-----------')) #Result:True
print(a.startswith('---------------------------')) #Result: False
print(a.startswith('Bell')) #Result: False

#Starts with - tuples Format
a = 'Hello world  I am Python'
print(a.startswith(("Hello", "HI", "Good Morning"))) #Result: True

b = 'HI world  I am Python'
print(b.startswith(("Hello", "HI", "Good Morning"))) #Result: True

c = 'Good world  I am Python'
print(c.startswith(("Hello", "HI", "Good Morning"))) #Result: False




#Ends with - tuples Format
a = 'Hello world  I am Python'
print(a.endswith(("Hello", "HI", "Python"))) #Result: True

b = 'HI world  I am Java'
print(b.endswith(("Hello", "Java", "Python"))) #Result: True

c = 'Hello world  I am Python'
print(c.endswith(("Hello", "HI", "Good Morning"))) #Result: False

########Split
a = ('Good Morning World I am Python')
print(a.split()) #Result: ['Good', 'Morning', 'World', 'I', 'am', 'Python']
print(a.split('o')) #Result: ['G', '', 'd M', 'rning W', 'rld I am Pyth', 'n']
print(len(a.split())) #Result:6
print(len(a)) #Result: 30

print(a.split('World')) #Result:['Good Morning ', ' I am Python']

#Split – space, words
b = 'A B C D E'
print(b.split(" ", 2))  #Result:['A', 'B', 'C D E']


#####rsplit – space, words
b = 'A B C D E'
print(b.rsplit(" ", 2))  #Result: ['A B C', 'D', 'E']


#Join
a = ['A', 'B', 'C', 'D', 'E']
print(a)  #Result: ['A', 'B', 'C', 'D', 'E']
print(" ".join(a))      #Result: A B C D E
print("------".join(a)) #Result: A------B------C------D------E

#Find Method:
a = "Hello World I am Python"
print(a.find("o")) #Result: 4

#right find:
print(a.rfind("o")) #Result: 21


#index: #rindex
a = "Hello World I am Python"
print(a.index("o"))  #Result: 4
print(a.rindex("o")) #Result: 21

#String Method - isascii
a = "Hello World I am Python"
print(a.isascii()) #Result: True

#format
print("Hello {name1} and {name2}".format(name1='friend', name2='foo'))
#Result:Hello friend and foo

#Concatenation - Meaning combining
a = 'Hello'
b = 'World'
c = a +' '+ b
print(c) #Result:Hello World


#concatenate error
# age = 31
# text = 'My age is'
# print(text + age)
#Result: TypeError: can only concatenate str (not "int") to str


age = 31
text = 'My age is'
print(text+ ' ' +str(age)) #Type casting is used here

#How to give the 31 in the __
#format method: It will takes the argument(value) , places it where there is a placeholders {}
age = 31
text = 'I am {} years old'
print(text.format(age))

#format method: passing multiple placeholders
age = 31
school = 'ABCD UNIVERSITY'
text = 'I am {} years old. I study in {}'
print(text.format(age,school))


#another way
age = 31
school = 'ABCD UNIVERSITY'
text2 = 'I am {} years old. I study in {}'.format(age,school)
print(text2)


#fstring
age = 31
school = 'ABCD UNIVERSITY'
text2 = f'I am {age} years old. I study in {school}'
print(text2)
