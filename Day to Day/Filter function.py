students = [
    {"name": "Hermione", "house": "Griffindor"},
    {"name": "Harry", "house": "Griffindor"}
]
"""
griffindors = [
    student["name"] for student in students if student["house"] == "Griffindor"
]

for griffindor in sorted(griffindors):
    print(griffindor) """

def is_griffindor(s):
    return s["house"] == "Griffindor"

griffindors = filter(is_griffindor, students)

for griffindor in griffindors:
    print(griffindor["name"])