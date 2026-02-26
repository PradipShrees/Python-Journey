import re

name = input("Enter your name: ").strip()
matches = re.search(r"^(.+), *(.+)$",name)
# we are using (..)group. here (.+) means one or more character and , is used to separate first and last name and space is used to separate first and last name
# here we are using regex to validate the name and also to extract first and last name
# here .+ means one or more character and , is used to separate first and last name
# here ^ means start of string and $ means end of string so it will only match if there is a comma in between and there is some character before and after comma
if matches:
    name = matches.group(2) + " " + matches.group(1)
    # we are using return value of group to extract first and last name and then we are concatenating them in the correct order
    # and we are using 1 and 2 because group(0) is the whole string and group(1) is the first group and group(2) is the second group
    #different convention for group while indexing""""
"""  last, first =matches.groups()
    name =f"{first} {last}" """
print(f"Hello, {name}")