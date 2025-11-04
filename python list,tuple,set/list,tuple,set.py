
### LIST ###

mylist = ["apple", "banana", "cherry"]
# In this list start in 0 1 2 
# In this list Reverse in -3 -2 -1

#Lists are used to store multiple items in a single variable.
#Lists are created using square brackets:

# Python - Access List Items
list = ["apple", "banana", "cherry"]
print(list[1])
print(list[2])
print(list[-1])
print(list[0])
print(list[-2])
print(list[-3])

# Using for loop

for i in list:
    print(i)

# Using a While Loop

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# Looping Using List Comprehension

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# Python - Change List Items
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change a Range of Item Values

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Insert Items

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Python - Add List Items

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Extend List

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Remove Specified Item

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#  Del

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Clear the List

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

###  TUPLE ###

mytuple = ("apple", "banana", "cherry")

# Tuples are used to store multiple items in a single variable
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Tuple Length

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# type()

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

# Access Tuple Items

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Change Tuple Values

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Add Items

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

###   SET   ###

myset = {"apple", "banana", "cherry"}

# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.


