myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])

"""
obj means inner values like 
for x,obj in myfamily.items() means 
	•	myfamily.items() returns pairs like:
	•	("child1", {"name": "Emil", "year": 2004})
	•	So:
	•	x becomes "child1", "child2", "child3"
	•	obj becomes the inner dictionary for that child
later obj[y] means value of name like Emil
if you print just y it will print name,year
    
    
    """