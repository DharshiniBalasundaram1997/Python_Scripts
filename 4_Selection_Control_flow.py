#One way Selection
# Result will be True or False

"""order = 460
minumum_order = 500
delivery = 50

if order > minumum_order:
    delivery = 0

total_price = order + delivery
print(order)
print(delivery)
print(total_price)"""

#Two Way Selection:
"""marks = 45
passing = 40

if marks >= passing:
    print('congratulations, you have passed')
else:
    print ('you have failed')
    
    
age = 19
if age <18:
    print('you are not eligible for vote')
else:
    print('you are eligible for vote')
"""


#Multi- Way Selection:
"""number = -10

if number > 0:
   print('+ve Number')
elif number == 0:
    print('zero / neutral number')
else:
   print("-ve Number")
"""


#Short Hand if
order = 500
minimum_order = 500
delivery = 50

total_price = order + delivery
if order > minimum_order: delivery = 0   #Short Hand if

print(total_price)

# Short Hand if .... else
#Ternary operators or conditional expressions
a = 10
print('Greater than 5') if a > 5 else print('Not Greater than 5') # Short Hand if .... else


# Logical Operators
# and
a = 90
b = 70
c = 100

if a > b and c > b: print("All the conditions were satisfied")
else: print('One or more conditions failed')

if a > b and c < b: print("All the conditions were satisfied")
else:print('One or more conditions failed')


# or
if a > b or c < b: print("All of the conditions were satisfied")
else: print('All conditions failed')

if a < b or c < b: print("All of the conditions were satisfied")
else: print('All conditions failed')


# not
if not(True):
    print('yes')
else:
    print('No')

if not(False):
    print('yes')
else:
    print('No')


number = 25
if number > 10:
   print('Greater than 10')
   if number > 20:
      print('Greater than 20')
   else:
      print('Not greater than 20')
else:
   print('Not Greater than 10')

##########Pass Keyword
number = 25
if number > 10:
    pass