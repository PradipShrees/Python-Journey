# Type hints are a way to indicate the expected data types of variables, function parameters, and return values in Python. They are not enforced by the Python interpreter but serve as a form of documentation and can be used by static type checkers to catch potential type errors.
def meow(number: int) -> int:
  for _ in range(number):
    print("Meow!")
number: int = int(input("Enter the number of meows: "))
if number <= 0:
  print("Please enter a positive integer.")
else:
  meow(number)
 
# : int is a type hint, it indicates that the variable number is expected to be of type int. It does not enforce the type, but it serves as a hint for developers and tools to understand the intended use of the variable.
# -> int is a type hint for the return type of the function meow, indicating that the function returns an integer.
# it doesn't affect the execution of the code, but it can help with code readability and can be used by static type checkers to catch potential type errors.


#TODO 1. Go to expression summery for more example of how
  #type hint is used better