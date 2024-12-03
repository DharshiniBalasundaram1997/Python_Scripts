"""#Sets: Sets  will store the multiple items and it use Curly brackets
# Items in the set in Unordered, Changeable, will not allow duplicates


#Items in the set is Unordered -
s1 = {'A','B','C','D'}
print(s1)  # Result:{'C', 'A', 'B', 'D'}  Each time we refresh,  the items will be unordered


#Sets will not allow duplicates - Set will not consider the duplicate values
s1 = {'A','B','C','D','D','D','D','D','D','D'}
print(s1)  # Result:{'C', 'A', 'B', 'D'} - Each time we refresh,  the items will be unordered
print(len(s1))  # Result:4


#Indexs cannot be used in Sets
#We cannot access the set by thuru the index value
# s1 = {'A','B','C','D','D','D','D','D','D','D'}
# print(s1[2])  # Result:  TypeError: 'set' object is not subscriptable


#How to access the index items in the set?:
#By using for loop we can access set index
s1 = {'A','B','C','D','D','D','D','D','D','D'}

for x in s1:
    print(x)
    # Result: Each time we refresh,  the items will be unordered
    # C
    # B
    # A
    # D

s1 = {'A','B','C','D','D','D','D','D','D','D'}
for x in s1:
    if x == 'A':
        print(x) # Result: A

s1 = {'A','B','C','D','C','D','D','D','D','D'}
for x in s1:
    if x == 'E':
        print(x)
    else:
        print("False" , end=" ") # Result: False False False False

#By using the membership operator also we can access the index items
S2 = {'A','B','C','D','D','D','D','D','D','D'}
print("B" in S2)  #Membership operator is used here      #Result: True
print("e" in S2) #Membership operator is used here       #Result: False
print("e" not in S2) #Membership operator is used here   #Result: True

#We can add , Update and remove the items in the set:
#Adding the items in the set
s1 = {'A','B','C','D'}
s1.add("Orange")
print(s1) #Result: {'Orange', 'D', 'C', 'B', 'A'} - Each time we refresh,  the items will be unordered


#Updating the items in the set
s1 = {'A','B','C','D'}
s2 = {10,20,30}
s1.update(s2)
print(s1) #Result: {10, 20, 30, 'C', 'D', 'B', 'A'} - Each time we refresh,  the items will be unordered


#Removing the items in the set - Discard method
s1 = {'A','B','C','D','E','F'}
s1.discard("E")
print(s1) #Result: {'F', 'A', 'C', 'D', 'B'} - Each time we refresh,  the items will be unordered

# Discard method will not raise an issue, even if the items are not present in set
s1 = {'A','B','C','D','E','F'}
s1.discard("ZZZ")
print(s1) #Result:{'E', 'D', 'F', 'C', 'A', 'B'} - Each time we refresh,  the items will be unordered

#Removing the items in the set -  remove method
s2 = {'A','B','C','D','E','F'}
s2.remove("E")
print(s2) #Result:{'F', 'A', 'C', 'D', 'B'} - Each time we refresh,  the items will be unordered

# Remove method will raise an issue,  if the items are not present in set
# s3 = {'A','B','C','D','E','F'}
# s3.remove("ZZZ")
# print(s3) #Result:KeyError: 'ZZZ'


#Pop method in set:
s1 = {'A','B','C','D','E','F'}
s1.pop()
print(s1) #Result:{'F', 'D', 'C', 'E', 'B'} - Each time we refresh,  the items in the pop will remove any items randomly. Bcoz the items are unordered

#clear method in set:
s1 = {'A','B','C','D','E','F'}
s1.clear()
print(s1) #Result: set() - It has given the empty set


#union in set: - union will combine both the set and give the result
# Only unique values will be displayed - Common values will not be repeated
s1 = {'A','B','C','D'}
s2 = {'C','D','E','F'}

s3 = s1.union(s2)
print(s3) #Result:{'A', 'C', 'D', 'E', 'B', 'F'} - Each time we refresh,  the items will be unordered



#intersection in set- only common values will be displayed
s1 = {'A','B','C','D'}
s2 = {'C','D','E','F'}

s3 = s1.intersection(s2)
print(s3) #Result: {'C', 'D'} - Each time we refresh,  the items will be unordered




#symmetric_difference in set - except common items- only unique values will be displayed
s1 = {'A','B','C','D'}
s2 = {'C','D','E','F'}

s3 = s1.symmetric_difference(s2)
print(s3) #Result:{'E', 'F', 'A', 'B'} - Each time we refresh,  the items will be unordered


#Subtraction in  set:
s1 = {'A','B','C','D'}
s2 = {'C','D','E','F'}

s3 = s1 - s2
print(s3) #Result:{'A', 'B'} - Each time we refresh,  the items will be unordered

s3 = s2 - s1
print(s3) #Result:{'F', 'E'} - Each time we refresh,  the items will be unordered


#Union in set - by using symbol (|) this is union symbol
s1 = {'A','B','C','D'}
s2 = {'C','D','E','F'}

s3 = s1|s2
print(s3) #Result:{'E', 'D', 'B', 'C', 'F', 'A'} - Each time we refresh,  the items will be unordered

#intersection in  set - by using symbol (&) this is intersection symbol:
s1 = {'A','B','C','D'}
s2 = {'C','D','E','F'}

s3 = s1 & s2
print(s3) #Result:{'D', 'C'} - Each time we refresh,  the items will be unordered
"""

