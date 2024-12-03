#Iterations:
#################While loop:
i = 0

while i <= 6:
    print(i)
    i += 1 #i = i + 1

#######################break keyword - stop
i = 0

while i <= 6:
    print(i)
    if i == 4:
        break
    i+= 1

#######################continue keyword - skip
i = 0
while i<=6:
    i +=1
    if i == 4:
        continue
    print(i)

#######################while - else statement:
i = 0
while i <=6:
    print(i)
    i += 1
else:
    print("i is no longer lesser than or equal to 6")


################## Iterations: for loop - sequences
l1 = [10, 20, 30, 40, 50]
print(type(l1)) #Result = [10,20,30,40,50]

l1 = [10, 20, 30, 40, 50]
print(l1* 2) #Result = [10,20,30,40,50,10,20,30,40,50]


# For loop in – Lists:
l1 = [10,20, 30, 40, 50]

for each_number in l1:
    print(each_number)


l1 = [10,20, 30, 40, 50]

for each_number in l1:
    print(each_number * 2)

# For loop in – Strings:
text = 'Hello World'
for each_character in text:
    print(each_character)

#for loop -  break keyword
l1 = [10,20, 30, 40, 50]

for each_number in l1:
    print(each_number * 2)
    if each_number == 30:
        break

#for loop -  continue keyword
l1 = [10,20, 30, 40, 50]

for each_number in l1:
    if each_number == 30:
        continue
    print(each_number * 2)

#for loop - if else -  continue keyword
l1 = [10,20, 30, 40, 50]

for each_number in l1:
    if each_number == 30:
        continue
    print(each_number)
else:
    print('Loop Complete')



#for loop - if else -  break keyword
l1 = [10,20, 30, 40, 50]

for each_number in l1:
    if each_number == 30:
        break
    print(each_number)
else:
    print('Loop Complete')





############Range Functions - It will return the Sequential of numbers
for x in range(5):
    print(x)

#Range Functions - Start and end
for x in range(2, 10):
    print(x)

#Range Functions - Start and end , Step
for x in range(2, 10, 2):
    print(x)

for x in range(2, 20, 5):
    print(x)








########### Nested Loops  - Inner Loop, Outer Loop
# Inner Loop will be executed one time for each item in the Outer Loop

colours = ['red', 'white', 'black']
transport = ['car', 'bike', 'scooter']

for each_colr in colours:
    for each_vechile in transport:
      print(each_colr)
      print(each_vechile)


# I need to print in same line:
colours = ['red', 'white', 'black']
transport = ['car', 'bike', 'scooter']

for each_colr in colours:
    for each_vechile in transport:
      print(each_colr, each_vechile)







#####################Assert True or False (Assertion Error)
x = 'hello'

assert x == ' hello'
# assert x == ' bye', 'X is  not a bye it is hello'





#########################Nested Loops - Using range Functions
for i in range(1, 5):
  # print(i)
  for j in range(i):
    print(i,end='')  #end='' => means no new line
    print() #new line

print(end='\n')



for i in range(1, 5):
  print(i)
  for j in range(i):
      print(i,end='')
      # print()


print(end='\n')
print(end='\n')

for i in range(1, 5):
  print(i)
  for j in range(i):
      print(i,end='')
      print()
print(end='\n')




for i in range(1, 5):
  # print(i)
  for j in range(i):
      print(i,end='')
      # print()

print(end='\n')