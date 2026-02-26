# Extracting Twitter Username from URL using Sub Method
# re.sub(pattern, replacement, string,count=0,flags=0) is used to replace the pattern with the replacement in the string
import re

url = input("Enter URL: ").strip()

username =re.sub(r"^(https?://)?(www\.)?twitter\.com/","", url)
# while writing regex for url we have to escape the dot because dot is a special character in regex and it matches any character except new line so we have to escape it to match the dot in the url
#username = url.replace("https://twitter.com/","")
## here we are using replace method to remove the different variations of twitter url and then we are using split method to split the url by / and then we are taking the first element of the list which is the username
# here we are using strip method to remove any leading or trailing whitespace from
print(f"Username: {username}")
# while expression is used anywhere we can complile diffrent expression special characters to get what we need.
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