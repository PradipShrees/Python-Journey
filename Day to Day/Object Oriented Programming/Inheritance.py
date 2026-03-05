# Inheritance allows us to create a new class that is a modified version of an existing class.
# In this example, we have a base class called Wizard, and two derived classes called Student and Professor. The Student and Professor classes inherit from the Wizard class, which means they can use the attributes and methods defined in the Wizard class.
# The Wizard class has an __init__ method that initializes the name attribute. The Student class has its own __init__ method that calls the __init__ method of the Wizard class using super() to initialize the name attribute, and also initializes the house attribute. 
# The Professor class does the same for the subject attribute.
# We then create instances of the Student and Professor classes and print out their attributes in the main function. This demonstrates how inheritance allows us to reuse code and create a hierarchy of classes.
# Note: The Wizard class raises a ValueError if the name is empty, ensuring that every wizard must have a name. This is an example of input validation in object-oriented programming.
#TODO: Add more attributes and methods to the Wizard class, such as a method to cast spells or a method to display the wizard's information. 
# Then, you can override these methods in the Student and Professor classes to provide specific implementations for each type of wizard.

# Wizard is a super class (or base class) that defines common attributes and methods for all wizards.
# like name and a method to display the wizard's information.

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

student = Student("Harry", "Gryffindor")  
professor = Professor("Severus", "Defense Against the Dark Arts")

def main():
    print(f"{student.name} is a student in {student.house}.")
    print(f"{professor.name} is a professor of {professor.subject}.")
    print(f"Name of Wizard is : {professor.name}")
if __name__ == "__main__":
    main()