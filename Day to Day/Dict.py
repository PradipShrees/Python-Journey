thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)
x = thisdict.get("colors")
x1 = tuple(x)
print(f"This is colors {x1}")
print(len(thisdict))
"""
.items prints all items in tuple form
.popitem() removes last inserted(doesn't work on py version 3.6 for before)
del deletes whole dict
.clear - clears all items from dict
.pop removes item with specified key name
.copy() to copy dict or use x = dict(thisdict) to make copy of dict



"""

"""
You can loop through dict using different methods like
1. for x in thisdict.values():
  print(x)

2. for x in thisdict.keys():
  print(x)

3. for x, y in thisdict.items():
  print(x, y)

  this will loop through all items with both key and value

4. simple looping using for loop
like 
for x in thisdict:
  print(x)
Note: this will loop through dict keys

clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""