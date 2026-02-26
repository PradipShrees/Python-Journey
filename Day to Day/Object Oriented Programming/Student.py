def main():
    student = get_students()
   """ if student[0] == "Padma":
        student[1] = "Raven claw"
         if you add this line this will give an error because tuple is immutable and we cannot change the value of a tuple once it is created.
         if you want to change the value of a tuple you have to create a new tuple with """
    print(f"{student[0]} is from {student[1]}")
    # here we are using indexing to access the elements of the tuple returned by the get_students function. 
    # student[0] is the name and student[1] is the house.
    #  we can also use tuple unpacking to assign the values to name and house variables in one line.

def get_students():
    name = input("Name: ").strip()
    house = input("House: ").strip()
    return (name, house)
# tuple is used when you want to return a inmutable sequence of values from a function.
# tuple is a collection which is ordered and unchangeable. In python tuples are written with round brackets.
# tuple unpacking is a feature in python that allows us to assign values from a tuple to variables in a single line.
# here we are returning a tuple from the function get_students and then we are unpacking the tuple into name and house variables in the main function.

if __name__ == "__main__":
# Only run this code when this file is executed directly (python file.py).
# If the file is imported (import file), this block will NOT run.
# This lets the file be both a reusable module and a runnable script entry point.
    main()