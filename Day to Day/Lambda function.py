# Lambda function is an anonymous function that can have any number of arguments but only one expression.
# It is defined using the lambda keyword.  
# Syntax: lambda arguments: expression

# Example 1: A lambda function that adds two numbers
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

# Example 2: A lambda function that squares a number
square = lambda x: x ** 2
print(square(4))  # Output: 16

# Example 3: A lambda function that checks if a number is even
is_even = lambda x: x % 2 == 0
print(is_even(10))  # Output: True
print(is_even(7))   # Output: False
# Example 4: A lambda function used with the map() function to square a list of numbers
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Example 5: A lambda function used with the filter() function to filter out even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]    

# Eaxmple 6 : A lambda function used with the sort() method to sort a list of tuples based on the second element
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

"""
So it's equivalent to writing:
python
def get_second(pair):
    return pair[1]

pairs.sort(key=get_second)
"""