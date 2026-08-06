# Operator Overloading

class Vault:
    def __init__(self, galleons=0, sickles =0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        # Here value is stored in the object (self) and can be accessed later using self.galleons, self.sickles, self.knuts
        # Value is passed from Right to Left (parameters to object attributes)
    def __str__(self):
        return f"{self.galleons} galleons, {self.sickles} sickles, {self.knuts} knuts"    

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)
potter = Vault(100, 50, 25)

print(potter)

weasley = Vault(50, 25, 10)
print(weasley)

total = f"\nTotal: {potter + weasley}"
print(total)

""" 
***HOW __init__ WORKS IN PYTHON OBJECT CREATION***
WHAT HAPPENS IN THIS PROGRAM (VISUAL)
=====================================

1) CREATE potter OBJECT
-----------------------
Code:
    potter = Vault(100, 50, 25)

__init__ is called with temporary parameter values:
    __init__(self=?, galleons=100, sickles=50, knuts=25)

self points to the new object (potter), then values are stored:
    potter.galleons = 100
    potter.sickles  = 50
    potter.knuts    = 25

potter object in memory:
┌─────────────────────┐
│ galleons: 100        │
│ sickles : 50         │
│ knuts   : 25         │
└─────────────────────┘


2) CREATE weasley OBJECT
------------------------
Code:
    weasley = Vault(50, 25, 10)

__init__ stores values in a different object:
    weasley.galleons = 50
    weasley.sickles  = 25
    weasley.knuts    = 10

weasley object in memory:
┌─────────────────────┐
│ galleons: 50         │
│ sickles : 25         │
│ knuts   : 10         │
└─────────────────────┘


3) ADD OBJECTS: potter + weasley
--------------------------------
Code:
    potter + weasley

Python translates this to:
    potter.__add__(weasley)

Inside __add__(self, other):
    self  = potter
    other = weasley

So it calculates totals (temporary local variables):
    galleons = self.galleons + other.galleons = 100 + 50 = 150
    sickles  = self.sickles  + other.sickles  = 50  + 25 = 75
    knuts    = self.knuts    + other.knuts    = 25  + 10 = 35

Then it RETURNS a NEW Vault object:
    return Vault(150, 75, 35)


4) NEW OBJECT CREATED: (result of addition)
-------------------------------------------
This creates a third object (a brand new Vault):

total_vault object in memory (the result):
┌─────────────────────┐
│ galleons: 150        │
│ sickles : 75         │
│ knuts   : 35         │
└─────────────────────┘


5) PRINTING
-----------
When you do:
    print(potter)
Python calls:
    potter.__str__()
and it reads stored values inside potter.

When you do:
    print(weasley)
Python calls:
    weasley.__str__()

When you do:
    f"{potter + weasley}"
- (potter + weasley) produces the NEW Vault object (150,75,35)
- then __str__ runs on that new object to turn it into text

FINAL PICTURE: 3 SEPARATE OBJECTS
=================================
potter object         weasley object         result object (potter+weasley)
┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│ g: 100        │      │ g: 50         │      │ g: 150        │
│ s: 50         │      │ s: 25         │      │ s: 75         │
│ k: 25         │      │ k: 10         │      │ k: 35         │
└──────────────┘      └──────────────┘      └──────────────┘
"""