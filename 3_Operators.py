############Arithmetic Operators:
x = 10
y = 5

print(x + y)
print(x - y)
print(x * y)
print(x / y) # Division will give quotient value
print(x % y) # Modulus will give reminder value
print(x ** y) #Raised to the power of exponential

print(x // y)  # Floor Division will give quotient value and ignore the decimal value
print(10 // 3)



############Assignment Operators
x= 10
print(x) #Result = 10


#Addition
x = x + 5 #Result = 10 + 5
print(x) #Result = 15

x+= 5  #Result = 15 + 5
print(x) #Result = 20


#Subtraction
x =  x - 5 #Result = 20 - 5
print(x) #Result = 15

x -= 5  #Result = 15- 5
print(x) #Result = 10



#Multiplication
x*= 5    #Result = 10 * 5
print(x)  #Result = 50



#Division
x/= 5    #Result = 50 / 5
print(x)  #Result = 10.0


#Modulus
x%= 5    #Result = 10.0 % 5
print(x)  #Result = 0.0

#Exponential
e = 10
e**= 5    #Result = 10 * 10 * 10 * 10 * 10
print(e)  #Result = 100000




###########Comparision Operator

#Equals
x = 10
print(x==10)

#Not equal to
print(x!=10)

#Greater  Than
print(x>10)

#Lesser Than
print(x<10)

#Greater than Equal to
print(x>=10)

#Lesser than Equal to
print(x<=10)


########Logical Operator

#and
y = 10
print(y > 5 and y < 20) # both the condition should satisfies, then will throw true
print(y > 5 and y < 9) # if one condition is not satisfied, then will throw false


#or
y = 10
print(y > 5 or y < 9)
print(y > 20 or x == 10)

#not
z = 10
print(not(z == 10))
print(not(z > 9))




###############Identity Operator

#is   #is not
x = ['apple', 'banana' ]
y = ['apple', 'banana' ]
z = x

print(x is y)
print(x is z)
print(y is not x)
print(x is not z)

p = 10
q = 4
print(p is q)
print(p is not q)


###############Membership Operator

#in    #not in
x = 'apple'
print('a' in x)
print('z' in x)
print('z' not in x)



###################BitWise Operator

#And Operator
x = 5 #binary value: 101
y = 3 #binary value: 011
result = x & y  # 101 & 011
print (result)  #result = 1

#OR Operator
result = x | y  # 101 | 011
print (result)  #result = 7


#XOR Operator
x = 5 #binary value: 101
y = 3 #binary value: 011
result = x ^ y  # 101 ^ 011
print (result)  #result = 6



#NOT Operator
x =5 #binary value: 101
y = 3 #binary value: 011
result = ~x  #010 (101 opposite of the binary value of x is 010)
print (result)  #result = -6




#Zero Fill LeftShit  Operator
x = 5 #binary value: 101
result = x << 3
print (result)  #result =40


#Zero Fill RightShit Operator
x = 5 #binary value: 101
result = x >> 1
print (result)  #result = 2