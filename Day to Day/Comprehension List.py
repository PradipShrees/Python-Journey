thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# this is the shorter way to write the code above, 
# but it is not recommended to use this syntax for side effects like printing. 
# It is better to use a regular for loop for clarity and readability.


# another example of list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# newlist = [expression for item in iterable if condition == True]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello' for x in fruits]

print(newlist)

# this sets all the values in the new list to 'hello', regardless of the value of x in the original list.



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)

# this replaces "banana" with "orange" in the new list, while keeping all other values the same as in the original list.

