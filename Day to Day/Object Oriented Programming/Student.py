# if _ is present infront of a variable it is a convention to indicate that the variable is intended for internal use only,
#  it is not meant to be accessed from outside the class,
#  it is a way to indicate that the variable is private and should not be accessed directly from outside the class,
#  it is a way to indicate that the variable is an implementation detail and should not be accessed directly from outside the class.
class Student:
    #class is a blueprint for creating objects, it is a template for creating objects, it is a way to define a new data type
    def __init__(self,name,house):
        # This None make passing house optional, if we don't pass house it will be None, if we pass house it will be the value of house
        if not name or not house:
            raise ValueError("Missing name or house")
        # this gives us much more control over the data that we are storing in our class, we can validate the data before storing it in our class,
        #  we can also raise an error if the data is not valid
        self.name = name
       

        # self is instance variable, it is used to store the value of the instance variable
        self.house = house
    def __str__(self):
        return f"{self.name} from {self.house}"
    #getter
    @property
    def house(self):
        return self._house
    #setter 
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("You don't belong to our private house")
        self._house = house

        #here we are passing value of setter house to _house which is a internal variable,
        #  we are using _house to store the value of house,
        #  this way we can validate the value of house before storing it in _house,
        #  if the value of house is not valid we can raise an error and we won't store the invalid value in _house, this way we can ensure that the data we are storing in our class is valid.
# if we use .house instead of _house in setter, we will get into an infinite loop where it keeps calling the setter and it will keep calling itself until it runs out of memory, 
# this is called infinite recursion, this is why we use _house to store the value of house,
#  so that we can avoid infinite recursion and we can validate the value of house before storing it in _house.
def main():
    student = get_students()
    student.house = "Number four SYDNEY ROAD"
    print(student)
    

def get_students():
    name = input("Name: ")
    house = input("House: ")
    try:
            return Student(name, house)
    except ValueError:
        print("Missing name or house")
       
        # here student is an instance of the class Student, it is an object of the class Student, it
    # this is called a constructor, it is used to create an instance of the class
    

if __name__ == "__main__":
    main()