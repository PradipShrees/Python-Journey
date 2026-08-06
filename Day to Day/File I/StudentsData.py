import csv
Students = []
with open("Students.csv") as file:
    for line in file:
        Name, House = line.rstrip().split(",")

        student = {"Names": Name, "House": House}
        Students.append(student)
def get_name(student):
    return student["Names"]
for student in sorted(Students, key=get_name):
    print(f"{student['Names']} is in {student['House']}")
"""Ben is not sorted becouse opf BOM which means it has invisible white space 
that causes it to be sorted at last. to fix go to chatgpt hehehe:) 
Or you can code in Vs code and make csv in Vs Code"""


"""Instead of def get_name(student):
    return student["Names"]
you can use key=lambda student: student("Names") 
  lambda can handle multiple parameter
  like student,x,y: """

# lambda = a small "anonymous function" (a function without a name).
# It’s used when you need a simple function for a short moment, without defining it with `def`.

# In sorted(..., key=...), Python needs a function that extracts the value used for sorting.
# Here, the lambda takes ONE student dictionary and returns the student's name.
# So sorting happens based on that returned name.