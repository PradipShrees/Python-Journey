students = [
    {"name": "Harry", "house": "Hogswarts"},
    {"name": "Hermione", "house": "Slytherin"},
    {"name": "Ron", "house": "Gryffindor"  },
    {"name": "Draco", "house": "Slytherin"}
]

houses =set()  # Using a set to avoid duplicates
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)