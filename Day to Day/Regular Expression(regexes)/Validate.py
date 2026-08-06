"""re.search(pattern,flags=0 means parameter you can passiin to modify behaviour of expression)"""


import re

email = input("Enter your email: ").strip()
if re.search(r"^(\w|\s|\.)+@(\w+\.)?\w+\.(edu|com|gov|org)$", email, re.IGNORECASE):
# nowdays internet uses another version of this validation , search google or chatgpt for that
# eg of what most browsers uses --->/^[\w.!#$%&'*+/=?^`{|}~-]+@[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?(?:\.[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?)*$/i
#here () is used with ? so it means optional(0 or more)
#if re.search(r"^(\w|\s)+@\w+\.(edu|com|gov|org)$", email.lower()): this could be done so we email becomes all lower case but we can use flags as well
# you can add different expression in one parameter
#if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):

#if re.search(r"^[^@]+@[^@]+\.edu$", email):
    # [a-zA-Z0-9_] means email will only except character on this range.
    # [^@] this means any character except @
    #$ means your email must end with .edu
    # ^ means 
   # here r means raw string literal so after \.edu is searched as it is
    # here ..* can be used instead of .+ , its same
    print("Valid email")
else:
    print("Invalid email")

"""
A|B either A or B this can be used to match different parameter like gov|com|org
(...) a group
(?:....) non-capturig version
\d decimal digit
\D not a decimal digit
\s whitespace characters
\S not a whitespace character
\w word as wellas numbers and underscore
\W not a word character
[] set of characters
[^] complementing(not include) set
^ matches the start of string
$ matches the end of string or just before the newline at the end of the string
* means there can be o or more repetition
+ means there can be 1 or more repetition
. means any character except new line
? means 0 or 1 repetition
{m} means m repetitions
{m-n} means m-n repititions
"""