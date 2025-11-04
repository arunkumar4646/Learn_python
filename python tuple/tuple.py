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