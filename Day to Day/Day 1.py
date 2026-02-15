import sys

print(sys.version)

print('mARY\'s dog said "woof"!')
"""This blacklash tell interpreter not to use 
' after it to not read it as code"""
Quantity = 32
Apple = 20
x = f"Sub total: {Apple * Quantity} "
print(x)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = "John"
print(x, y)

x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)